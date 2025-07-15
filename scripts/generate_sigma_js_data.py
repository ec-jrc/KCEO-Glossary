import os
import re
import json
import random # MOVED IMPORT TO THE TOP
from files_to_exclude import files_to_exclude

# --- Configuration ---
DOCS_DIRECTORY = './docs/terms'
OUTPUT_JS_FILE = os.path.join("./docs/assets/sigmajs/", 'sigma_graph_data.js')
DEFAULT_NODE_COLOR = "#5A75DB"
DEFAULT_NODE_SIZE = 10
DEFAULT_EDGE_COLOR = "#ccc"
DEFAULT_EDGE_TYPE = "arrow"
DEFAULT_EDGE_SIZE = 1

# --- Helper Functions ---

def sanitize_for_node_id(text):
    """Creates a JavaScript-friendly ID from a string."""
    if not text:
        return "unknown_node"
    # Replace spaces and special characters with underscores, convert to lowercase
    s = re.sub(r'\s+', '_', text.strip())
    s = re.sub(r'[^a-zA-Z0-9_-]', '', s)
    s = re.sub(r'_+', '_', s) # Collapse multiple underscores
    s = s.strip('_')
    return s.lower() if s else "unnamed_node"

def get_h1_title_and_path(file_path):
    """Extracts the first H1 title and returns it along with the file's basename without extension."""
    base_name_no_ext = os.path.splitext(os.path.basename(file_path))[0]
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            for line in content.splitlines():
                stripped_line = line.strip()
                if stripped_line.startswith('# ') and not stripped_line.startswith('##'):
                    title_text = stripped_line.lstrip('# ').strip()
                    # Extract text from link if title is already a link
                    title_text = re.sub(r'\[([^\]]+)\]\(.*?\)', r'\1', title_text)
                    # Remove common markdown formatting (bold, italics, code)
                    title_text = re.sub(r'[*_`]', '', title_text)
                    return title_text.strip(), base_name_no_ext
    except FileNotFoundError:
        print(f"Warning: File not found while getting H1: {file_path}")
    except Exception as e:
        print(f"Error reading H1 from {file_path}: {e}")
    # Fallback if no H1 found or error
    return base_name_no_ext.replace("_", " ").capitalize(), base_name_no_ext


def get_first_definition_text(file_path):
    """Extracts content under '## 1 Definition' until the next H2 or specific H3."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        lines = content.splitlines()
        in_definition = False
        definition_lines = []
        for line in lines:
            if line.strip().startswith('## 1 Definition'):
                in_definition = True
                continue
            if in_definition:
                if line.strip().startswith('## ') or \
                   line.strip().startswith('### Notes') or \
                   line.strip().startswith('### Examples') or \
                   line.strip().startswith('### Sources'):
                    break
                definition_lines.append(line)
        return "\n".join(definition_lines)
    except FileNotFoundError:
        # print(f"Warning: File not found for definition extraction: {file_path}")
        return ""
    except Exception as e:
        print(f"Error extracting definition from {file_path}: {e}")
        return ""

def extract_definition_links(definition_text, current_file_basename_no_ext):
    """Extracts valid glossary link targets (basenames) from definition text."""
    link_pattern = re.compile(r'\[(?:[^\]]+?)\]\((.+?)\)')
    found_target_basenames = []
    for match in link_pattern.finditer(definition_text):
        link_url = match.group(1)
        if link_url.startswith('../') and not any(link_url.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.html']):
            # --- CORRECTED LINE ---
            # Split the path and take the last part, which is the filename/term
            target_basename = link_url.split('/')[-1]
            
            if target_basename and target_basename != current_file_basename_no_ext:
                found_target_basenames.append(target_basename)
    return list(set(found_target_basenames)) # Unique targets

# --- Main Logic ---
def main():
    nodes_data = {}  # Using dict for unique nodes: {node_id: {attributes}}
    edges_data = set() # Using set for unique edges: {(source_id, target_id)}
    
    # Mapping from filename_no_ext to its canonical H1 label and generated nodeId
    filename_to_node_info = {}

    md_files = [
        f for f in os.listdir(DOCS_DIRECTORY)
        if f.endswith('.md') and f not in files_to_exclude
    ]

    # Pass 1: Discover all nodes and map filenames to H1 titles and node IDs
    print("Pass 1: Discovering nodes and mapping H1 titles...")
    for md_file_name in md_files:
        file_full_path = os.path.join(DOCS_DIRECTORY, md_file_name)
        h1_label, basename_no_ext = get_h1_title_and_path(file_full_path)
        
        if not h1_label: 
            print(f"Critical: Could not determine H1/label for {md_file_name}")
            h1_label = basename_no_ext.replace("_", " ").capitalize()

        node_id = sanitize_for_node_id(h1_label)
        
        filename_to_node_info[basename_no_ext] = {
            "id": node_id,
            "label": h1_label,
            "link_path": basename_no_ext
        }
        
        if node_id not in nodes_data:
            nodes_data[node_id] = {
                "id": node_id,
                "label": h1_label,
                "x": round(random.random() * 100, 2), 
                "y": round(random.random() * 100, 2),
                "size": DEFAULT_NODE_SIZE,
                "color": DEFAULT_NODE_COLOR,
                "link_path": basename_no_ext
            }

    # Pass 2: Extract links from definitions and create edges
    print("\nPass 2: Extracting links from definitions and creating edges...")
    for md_file_name in md_files:
        file_full_path = os.path.join(DOCS_DIRECTORY, md_file_name)
        current_basename_no_ext = os.path.splitext(md_file_name)[0]

        source_node_info = filename_to_node_info.get(current_basename_no_ext)
        if not source_node_info:
            print(f"Warning: Source node info not found for {current_basename_no_ext}. Skipping its links.")
            continue
        
        source_node_id = source_node_info["id"]

        definition_text = get_first_definition_text(file_full_path)
        if not definition_text:
            continue

        linked_target_basenames = extract_definition_links(definition_text, current_basename_no_ext)

        for target_basename in linked_target_basenames:
            target_node_info = filename_to_node_info.get(target_basename)
            if target_node_info:
                target_node_id = target_node_info["id"]
                if source_node_id != target_node_id: 
                    edges_data.add((source_node_id, target_node_id))
            else:
                print(f"Warning: Linked target '{target_basename}' (from {md_file_name}) not found in filename_to_node_info map. Link ignored.")

    js_nodes = list(nodes_data.values())
    js_edges = [
        {"source": s_id, "target": t_id, "type": DEFAULT_EDGE_TYPE, "color": DEFAULT_EDGE_COLOR, "size": DEFAULT_EDGE_SIZE}
        for s_id, t_id in sorted(list(edges_data))
    ]

    js_output_parts = [
        "const sigmaGraphData = {",
        f"  nodes: {json.dumps(js_nodes, indent=2)},", # Added indent for readability
        f"  edges: {json.dumps(js_edges, indent=2)}",  # Added indent
        "};",
        "",
        "// This function will be called by sigmajs.md to load data into a Graphology instance",
        "function loadSigmaGraph(graphInstance) {",
        "  if (!graphInstance) {",
        "    console.error('Graphology instance not provided to loadSigmaGraph.');",
        "    return;",
        "  }",
        "  sigmaGraphData.nodes.forEach(nodeData => {",
        "    if (!graphInstance.hasNode(nodeData.id)) {",
        "      graphInstance.addNode(nodeData.id, { ...nodeData });", # Spread nodeData for attributes
        "    }",
        "  });",
        "  sigmaGraphData.edges.forEach(edgeData => {",
        "    if (!graphInstance.hasEdge(edgeData.source, edgeData.target)) {",
        "      try { graphInstance.addEdge(edgeData.source, edgeData.target, { ...edgeData }); }", # Spread edgeData
        "      catch (e) { /* Edge might exist in other direction if graph is undirected by default, or other issues */ }",
        "    }",
        "  });",
        "}"
    ]
    
    final_js_output = "\n".join(js_output_parts)

    try:
        with open(OUTPUT_JS_FILE, "w", encoding="utf-8") as f:
            f.write(final_js_output)
        print(f"\nSuccessfully generated {OUTPUT_JS_FILE} with {len(js_nodes)} nodes and {len(js_edges)} edges.")
    except Exception as e:
        print(f"Error writing to {OUTPUT_JS_FILE}: {e}")

if __name__ == "__main__":
    if not os.path.exists(DOCS_DIRECTORY):
        print(f"Error: Docs directory '{DOCS_DIRECTORY}' not found from CWD ({os.getcwd()}). Make sure you are running the script from the project root.")
    else:
        main()