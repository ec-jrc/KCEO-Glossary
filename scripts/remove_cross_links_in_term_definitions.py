import re
import os
from files_to_exclude import files_to_exclude

# Change the working directory to 'docs/'
os.chdir("./docs/terms/")

# Function to remove relative links from the provided file paths
def remove_relative_links(file_paths):
    # Regex pattern to match markdown links
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        def replace_link(match):
            text = match.group(1)
            url = match.group(2)
            # Check if the URL is a relative link (does not contain http or https)
            if not url.startswith(('http://', 'https://')):
                return text  # Return only the text, removing the link
            return match.group(0)  # Return the whole match unchanged

        # Process content to remove relative links
        new_content = re.sub(link_pattern, replace_link, content)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

if __name__ == "__main__":
    # List all .md files in the current directory
    all_md_files = [file for file in os.listdir() if file.endswith('.md')]

    file_paths_to_process = [file for file in all_md_files if file not in files_to_exclude]

    # Process the remaining files
    remove_relative_links(file_paths_to_process)

    print("Cross references removed successfully.")

    # Example usage
    # file_paths = ["in-situ_observation.md","information.md","introduction.md","location.md","measurand.md","measurement.md","observation.md","uncertainty.md"]
    # files_to_exclude =["changelog.md","impressum.md","index.md", "introduction.md","mermaid.md"]
    # file_paths = ["uncertainty.md"]

