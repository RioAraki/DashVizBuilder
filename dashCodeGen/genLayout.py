def button_layout(node):
    data = node["data"]

    id = data.get("id", "")

    return f"""
html.Button(
    "{id}",
    id="{id}",
    n_clicks=0
)
"""


def input_layout(node):
    data = node["data"]
    id = data.get("id", "")
    type = data.get("type", "")
    placeholder = data.get("placeholder", "")
    value = data.get("value", "")

    return f"""
dcc.Input(
    id="{id}",
    type="{type}",
    placeholder="{placeholder}",
    value="{value}"
)
"""


def div_layout(node):
    data = node["data"]
    id = data.get("id", "")

    return f"""
html.Div(
    id="{id}"
)
"""

def div_wrap(content):

    return f"""
    html.Div(
        children=[
            {content}
        ],
    ),
"""

def generate_layout(nodes):
    content = """"""


    for node in nodes.get_all():
        if node["type"] == "button":
            content += div_wrap(button_layout(node))
        elif node["type"] == "input":
            content += div_wrap(input_layout(node))
        elif node["type"] == "div":
            content += div_wrap(div_layout(node))

    result = f"""
from dash import dcc, html

layout = html.Div(
    children=[
        {content}
    ],
    style={{'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}}
)
"""
        
    with open("./output/layout.py", "w") as file:
        file.write(result)
