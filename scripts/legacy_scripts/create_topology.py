import re
from collections import defaultdict

# Helper function to parse the mermaid markdown and extract relationships
def parse_mermaid_relationships(mermaid_content):
    # Adjusted regex pattern
    pattern = re.compile(r'id_([\w-]+)\(\["<a href=\'\.\./([\w-]+)\'>([\w\s-]+)</a>"\]\) --> id_([\w-]+)\(\["<a href=\'\.\./([\w-]+)\'>([\w\s-]+)</a>"\]\)')
    relationships = defaultdict(lambda: {'parents': set(), 'children': set(), 'link': None})

    for match in pattern.finditer(mermaid_content):
        parent_id, parent_link, parent_name, child_id, child_link, child_name = match.groups()

        # Add child to parent's children list
        relationships[parent_name]['children'].add((child_name, f"../{child_link}/"))
        relationships[parent_name]['link'] = f"../{parent_link}/"  # Add link for parent

        # Add parent to child's parents list
        relationships[child_name]['parents'].add((parent_name, f"../{parent_link}/"))
        relationships[child_name]['link'] = f"../{child_link}/"  # Add link for child

    return relationships

# Read the mermaid.md file
with open('docs/mermaid.md', 'r') as file:
    mermaid_content = file.read()

# Remove leading and trailing backticks and optional whitespace/newlines
mermaid_content = mermaid_content.strip('` \n')

# Parse relationships
relationships = parse_mermaid_relationships(mermaid_content)

# Write the glossary_topology.md file
with open('docs/glossary_topology.md', 'w') as file:
    for term, links in sorted(relationships.items()):
        file.write(f'## [{term}]({links["link"]})\n')  # Make heading a hyperlink
        if links['parents']:
            file.write('**Parents**: ')
            file.write(', '.join(f"[{parent[0]}]({parent[1]})" for parent in sorted(links['parents'])))
            if links['children']:
                file.write('<br>\n')
            else:
                file.write('\n')
        if links['children']:
            file.write('**Children**: ')
            file.write(', '.join(f"[{child[0]}]({child[1]})" for child in sorted(links['children'])))
            file.write('\n')
        file.write('\n')

print('glossary_topology.md has been created/overwritten with the extracted relationships.')
