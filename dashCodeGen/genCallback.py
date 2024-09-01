def generate_callback(nodes, edges):
    callbacks = """"""

    for node in nodes.get_all():
        if node["type"] == "callback":
            callback_id = node["id"]
            callback_name = node["data"]["id"]
            input_deco = []
            state_deco = """"""
            output_deco = """"""
            parameters = ""

            for edge in edges.get_edges_by_source(callback_id):
                output_deco += f"""Output("{nodes.get_node_by_id(edge['target'])['data']['id']}", "{edge['targetHandle']}"),"""
            for edge in edges.get_edges_by_target(callback_id):
                if edge["targetHandle"] == "input":
                    input_deco.append(f"""Input("{nodes.get_node_by_id(edge['source'])['data']['id']}", "{edge['sourceHandle']}"),""")
                else:
                    state_deco += f"""State("{nodes.get_node_by_id(edge['source'])['data']['id']}", "{edge['sourceHandle']}"),"""
                parameters += f"{nodes.get_node_by_id(edge['source'])['data']['id']}, "
                callback_text = (f"""
    @app.callback(
        {output_deco}
        {"\n        ".join(input_deco)}
        {state_deco}
        )
    def {callback_name}({parameters}):
        pass # fill in the actual business logic here
"""
)
                
            callbacks += callback_text
                
           
    content = f"""
import dash
from dash import Input, Output, State

def register_callbacks_to_app(app):
{callbacks}
"""

    with open("./output/callback.py", "w") as file:
        file.write(content)