import json
import argparse
from genApp import generate_app
from genCallback import generate_callback
from genLayout import generate_layout
from util.edges import Edges
from util.nodes import Nodes

def main():

    parser = argparse.ArgumentParser(description="Generate app, layout, and callbacks from JSON file.")
    parser.add_argument('json_filename', type=str, help="The JSON file containing the nodes and edges.")

    args = parser.parse_args()

    with open(args.json_filename, 'r') as file:
        data = json.load(file)

        nodes = Nodes(data["nodes"])
        edges = Edges(data["edges"])
        
        generate_app()
        generate_layout(nodes)
        generate_callback(nodes, edges)

if __name__ == "__main__":
    main()