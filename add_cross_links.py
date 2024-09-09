import os
import re

def extract_titles_from_md(file_path):
    titles = []
    with open(file_path, 'r') as file:
        in_yaml = False
        for line in file:
            if line.strip() == '---':
                in_yaml = not in_yaml
            if in_yaml:
                continue
            if line.startswith('# ') and not line.startswith('##'):
                # Remove "#" and any potential markdown link syntax
                title = re.sub(r'\[([^\]]+)\]\(.*?\)', r'\1', line.lstrip('# ').strip())
                titles.append(title)
    return titles

def insert_hyperlinks(file_path, terms):
    with open(file_path, 'r') as file:
        content = file.readlines()

    new_content = []
    in_yaml = False
    current_title = None

    for line in content:
        if line.strip() == '---':
            in_yaml = not in_yaml
            new_content.append(line)
            continue
        if in_yaml:
            new_content.append(line)
            continue
        if line.startswith('# ') and not line.startswith('##'):
            current_title = re.sub(r'\[([^\]]+)\]\(.*?\)', r'\1', line.lstrip('# ').strip())
            new_content.append(line)
            continue
        
        for term in terms:
            if term == current_title:  # Skip self-references
                continue
            
            # Skip terms that already have a hyperlink
            if re.search(r'\[' + re.escape(term) + r'\]\(.*?\)', line):
                continue
            
            # Avoid altering headings by ensuring replacements are only made in non-heading lines
            pattern = re.compile(r'\b' + re.escape(term) + r'\b', re.IGNORECASE)
            replacement = f'[{term}](../{" ".join(term.split()).lower()})'
            line = pattern.sub(lambda match: replacement if not re.search(rf'\[{re.escape(match.group(0))}\]\(.*?\)', match.string) else match.group(0), line)
        
        new_content.append(line)

    with open(file_path, 'w') as file:
        file.writelines(new_content)

def main(directory, exclude_files):
    all_titles = []
    md_files = [f for f in os.listdir(directory) if f.endswith('.md') and f not in exclude_files]

    # Extract titles from all markdown files
    for md_file in md_files:
        file_path = os.path.join(directory, md_file)
        titles = extract_titles_from_md(file_path)
        all_titles.extend(titles)

    # Insert hyperlinks based on extracted titles
    for md_file in md_files:
        file_path = os.path.join(directory, md_file)
        insert_hyperlinks(file_path, all_titles)

if __name__ == "__main__":
    directory = './docs'  # Replace with your directory path
    exclude_files = ['changelog.md', 'impressum.md', 'index.md', 'glossary.md', 'introduction.md', 'mermaid.md']  # Files to be excluded
    main(directory, exclude_files)