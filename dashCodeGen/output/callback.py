
import dash
from dash import Input, Output, State

def register_callbacks_to_app(app):

    @app.callback(
        Output("display", "children"),
        Input("increment", "n_clicks"),
        Input("reset", "n_clicks"),
        Input("offset", "value"),
        State("display", "children"),
        )
    def update_value(increment, reset, offset, display, ):
        pass # fill in the actual business logic here

