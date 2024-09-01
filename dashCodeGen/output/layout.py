
from dash import dcc, html

layout = html.Div(
    children=[
        
    html.Div(
        children=[
            
html.Button(
    "increment",
    id="increment",
    n_clicks=0
)

        ],
    ),

    html.Div(
        children=[
            
html.Button(
    "reset",
    id="reset",
    n_clicks=0
)

        ],
    ),

    html.Div(
        children=[
            
dcc.Input(
    id="offset",
    type="number",
    placeholder="",
    value=""
)

        ],
    ),

    html.Div(
        children=[
            
html.Div(
    id="display"
)

        ],
    ),

    ],
    style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}
)
