def button_layout(node):
    data = node["data"]

    buttonName = data.get("buttonName", "")

    return f"""
html.Button(
    "{buttonName}",
    id="button_{buttonName}",
    n_clicks=0
)
"""


def input_layout(node):
    data = node["data"]
    input_name = data.get("inputName", "")
    input_type = data.get("inputType", "")
    placeholder = data.get("placeholder", "")
    value = data.get("value", "")

    return f"""
dcc.Input(
    id="{input_name}",
    type="{input_type}",
    placeholder="{placeholder}",
    value="{value}"
)
"""


def div_layout(node):
    data = node["data"]
    div_id = data.get("divId", "")

    return f"""
html.Div(
    id="{div_id}"
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

def generate_layout(node_list):
    content = """"""



    for node in node_list:
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
