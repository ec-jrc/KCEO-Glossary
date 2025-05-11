import os
import re

def sanitize_node_id(term):
    # Replace spaces with underscores and prepend 'id_'
    return 'id_' + re.sub(r'\s+', '_', term.strip()).lower()

def format_node_label(term):
    # Replace underscores with spaces and capitalize all words
    return ' '.join(word.capitalize() for word in term.split('_'))

def format_node_link(term):
    # Create the relative URL for the node
    return f'../{term.lower().replace(" ", "_")}'

def extract_relevant_section(content):
    # Extract the text between "## 1 Definition" and "### Notes"
    pattern = re.compile(r'## 1 Definition(.*?)### Notes', re.DOTALL)
    match = pattern.search(content)
    if match:
        return match.group(1)
    return ""

def parse_markdown_files(directory, exclude_files):
    graph = {}
    md_link_pattern = re.compile(r'\[([^\]]+)\]\(([^\)]+)\)')

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md') and file not in exclude_files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    relevant_section = extract_relevant_section(content)
                    matches = md_link_pattern.findall(relevant_section)
                    for match in matches:
                        term, link = match
                        # Skip internet links and links with file extensions such as .html
                        if link.startswith('http://') or link.startswith('https://') or link.endswith('.html'):
                            continue
                        link = os.path.normpath(link.strip('/'))
                        parent_file = link + '.md'
                        if os.path.basename(parent_file) not in exclude_files:
                            if parent_file not in graph:
                                graph[parent_file] = set()
                            graph[parent_file].add(file)

    return graph

def create_mermaid_diagram(graph):
    mermaid_diagram = "flowchart TD;\n"
    node_ids = {}  # Store the sanitized node ids
    for parent, children in graph.items():
        parent_node = os.path.splitext(os.path.basename(parent))[0]
        parent_node_id = sanitize_node_id(parent_node)
        parent_node_label = format_node_label(parent_node)
        parent_node_link = format_node_link(parent_node)
        node_ids[parent_node] = parent_node_id
        for child in children:
            child_node = os.path.splitext(os.path.basename(child))[0]
            child_node_id = sanitize_node_id(child_node)
            child_node_label = format_node_label(child_node)
            child_node_link = format_node_link(child_node)
            node_ids[child_node] = child_node_id
            mermaid_diagram += (
                f'    {parent_node_id}(["<a href=\'{parent_node_link}\'>{parent_node_label}</a>"]) --> '
                f'{child_node_id}(["<a href=\'{child_node_link}\'>{child_node_label}</a>"]);\n'
            )
    return mermaid_diagram

def main(directory, exclude_files):
    graph = parse_markdown_files(directory, exclude_files)
    mermaid_diagram = create_mermaid_diagram(graph)
    with open('docs/mermaid.md', 'w') as f:
        f.write('```mermaid\n')
        f.write(mermaid_diagram)
        f.write('```\n')

if __name__ == "__main__":
    directory = './docs'  # Replace with your directory path
    exclude_files = ['changelog.md', 'impressum.md', 'index.md', 'glossary.md', 'introduction.md', 'mermaid.md']  # Files to be excluded
    main(directory, exclude_files)
