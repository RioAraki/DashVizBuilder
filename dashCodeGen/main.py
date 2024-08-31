import json
import argparse
from genApp import generate_app
from genCallback import generate_callback
from genLayout import generate_layout

# Set up command-line argument parsing
parser = argparse.ArgumentParser(description="Generate app, layout, and callbacks from JSON file.")
parser.add_argument('json_filename', type=str, help="The JSON file containing the nodes and edges.")

# Parse the command-line arguments
args = parser.parse_args()

# Load the JSON file
with open(args.json_filename, 'r') as file:
    data = json.load(file)

    node_list = [node for node in data["nodes"]]
    edge_list = [edge for edge in data["edges"]]
    
    generate_app()
    generate_layout(node_list)
    generate_callback(node_list, edge_list)
