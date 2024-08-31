def generate_callback(node_list, edge_list):
    content = """
import dash
from dash import Input, Output, State

def register_callbacks_to_app(app):
    pass
    """

    with open("./output/callback.py", "w") as file:
        file.write(content)