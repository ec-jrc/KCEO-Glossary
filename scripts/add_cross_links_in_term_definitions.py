import os
import re

def extract_titles_from_md(file_path):
    """Extracts H1 titles from a markdown file, stripping common markdown formatting."""
    titles = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            in_yaml_front_matter = False
            for line in file:
                stripped_line = line.strip()
                if stripped_line == '---':
                    in_yaml_front_matter = not in_yaml_front_matter
                    continue
                if in_yaml_front_matter:
                    continue
                
                if line.startswith('# ') and not line.startswith('##'):
                    title_text = line.lstrip('# ').strip()
                    # Extract text from link if title is already a link
                    title_text = re.sub(r'\[([^\]]+)\]\(.*?\)', r'\1', title_text)
                    # Remove common markdown formatting (bold, italics, code) from the title itself
                    title_text = re.sub(r'[*_`]', '', title_text) 
                    titles.append(title_text.strip())
    except FileNotFoundError:
        print(f"Warning: File not found while extracting titles: {file_path}")
    return titles

def insert_hyperlinks(file_path, all_terms_list, current_file_h1_titles_normalized):
    """
    Inserts hyperlinks into a markdown file.
    Prioritizes longest matches, handles simple plurals (ending in 's' or 'es'),
    and avoids re-linking or linking within existing links.
    """
    # Sort all available terms by length in descending order.
    # This is crucial for the logic that finds all potential matches later.
    sorted_terms_for_linking = sorted(all_terms_list, key=len, reverse=True)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content_lines = file.readlines()
    except FileNotFoundError:
        print(f"Warning: File not found during insert_hyperlinks: {file_path}")
        return

    new_content_lines = []
    in_yaml_front_matter = False

    for line_text in content_lines:
        stripped_line_for_check = line_text.strip()
        if stripped_line_for_check == '---':
            in_yaml_front_matter = not in_yaml_front_matter
            new_content_lines.append(line_text)
            continue
        if in_yaml_front_matter:
            new_content_lines.append(line_text)
            continue
        
        # Skip modifying any heading lines for actual term replacement
        if line_text.startswith('#'):
            new_content_lines.append(line_text)
            continue

        # --- Line processing using placeholder method for existing links ---
        
        # 1. Protect existing Markdown links in the current line
        original_links_in_line = []
        def _store_link_callback(match_obj):
            original_links_in_line.append(match_obj.group(0))
            # Using Private Use Area characters as placeholders
            return f"\uE000{len(original_links_in_line)-1}\uE001" 
        
        line_with_protected_links = re.sub(r'\[[^\]]*?\]\([^)]*?\)', _store_link_callback, line_text)
        
        # 2. Find all possible matches for all terms in the (now link-protected) line
        potential_link_matches = []
        for term_candidate_singular in sorted_terms_for_linking:
            # Skip self-referencing any H1 title of the current file (case-insensitive check)
            if any(term_candidate_singular.lower() == h1_norm.lower() for h1_norm in current_file_h1_titles_normalized):
                continue
            
            # Regex to match the term and its simple plural forms (term + s, term + es)
            # (?:es|s)? matches 'es' first if present, then 's', or nothing.
            term_pattern_regex = re.compile(
                r'\b' + re.escape(term_candidate_singular) + r'(?:es|s)?\b', 
                re.IGNORECASE
            )
            for match_obj in term_pattern_regex.finditer(line_with_protected_links):
                potential_link_matches.append({
                    "start": match_obj.start(),
                    "end": match_obj.end(),
                    "term_text_singular": term_candidate_singular, # Canonical term for link path
                    "matched_text_in_line": match_obj.group(0) # Actual matched text (could be plural)
                })

        # 3. Sort potential matches: by start position, then by length of term (longest singular form first)
        potential_link_matches.sort(key=lambda m: (m["start"], -len(m["term_text_singular"])))
        
        # 4. Build the new line by applying non-overlapping, longest-first replacements
        processed_line_parts = []
        current_char_index_in_line = 0
        for match_details in potential_link_matches:
            match_start_pos = match_details["start"]
            match_end_pos = match_details["end"]
            
            if match_start_pos >= current_char_index_in_line: # Non-overlapping
                # Append text from end of last match to start of current match
                processed_line_parts.append(line_with_protected_links[current_char_index_in_line:match_start_pos])
                
                # Create and append the hyperlink
                term_display_text = match_details["matched_text_in_line"]
                term_link_path_singular = match_details["term_text_singular"]
                # Use underscores for link path
                link_path_segment = "_".join(term_link_path_singular.split()).lower()
                hyperlink_markdown = f'[{term_display_text}](../{link_path_segment})'
                processed_line_parts.append(hyperlink_markdown)
                
                current_char_index_in_line = match_end_pos
        
        # Append any remaining part of the line (after the last processed match)
        processed_line_parts.append(line_with_protected_links[current_char_index_in_line:])
        final_line_with_new_links = "".join(processed_line_parts)
        
        # 5. Restore original links (that were protected at the start)
        restored_final_line = final_line_with_new_links
        for i, original_link_text in enumerate(original_links_in_line):
            placeholder_tag = f"\uE000{i}\uE001"
            restored_final_line = restored_final_line.replace(placeholder_tag, original_link_text)
            
        new_content_lines.append(restored_final_line)
        # --- End of line processing ---

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_content_lines)

def main(directory, exclude_files):
    all_extracted_titles = []
    # This script currently only processes files directly under the `directory`
    # It does not recurse into subdirectories unless `os.walk` is used.
    md_files_to_process = [f for f in os.listdir(directory) 
                           if f.endswith('.md') and f not in exclude_files]

    # First pass: Extract all H1 titles from all relevant markdown files
    for md_file_name in md_files_to_process:
        file_full_path = os.path.join(directory, md_file_name)
        titles_in_file = extract_titles_from_md(file_full_path)
        all_extracted_titles.extend(titles_in_file)
    
    # Create a unique list of canonical terms, sorted by length (desc) for matching preference
    unique_terms_canonical = sorted(list(set(t for t in all_extracted_titles if t.strip())), key=len, reverse=True)

    # Second pass: Insert hyperlinks into each file
    for md_file_name in md_files_to_process:
        file_full_path = os.path.join(directory, md_file_name)
        # Get H1 titles of the *current* file (normalized) to avoid self-linking its own main titles
        current_file_h1s_titles_only = extract_titles_from_md(file_full_path)
        current_file_h1s_normalized = [t.lower() for t in current_file_h1s_titles_only]
        
        insert_hyperlinks(file_full_path, unique_terms_canonical, current_file_h1s_normalized)
        #print(f"Processed cross-references for: {md_file_name}")

if __name__ == "__main__":
    docs_directory = './docs'
    # Files to be excluded from processing (directly under ./docs)
    files_to_exclude = [
        'changelog.md', 'impressum.md', 'index.md', 
        'glossary.md', 'introduction.md', 'mermaid.md', 
        'sigmajs.md', 'glossary_topology.md', 'tags.md',
        '_template.md' 
    ]
    # Note: To exclude files in subdirectories like 'blog/posts', the file discovery
    # in main() would need to use os.walk and the exclude_files list would need
    # to handle relative paths from 'directory' or absolute paths.
    # The current script structure primarily targets top-level markdown files in 'docs_directory'.

    main(docs_directory, files_to_exclude)
    print("Cross-referencing script finished.")