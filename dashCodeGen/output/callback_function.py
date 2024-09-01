
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
        ctx = dash.callback_context

        if not ctx.triggered:
            return "Current value: 0"
        else:
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]

            # Handle NoneType for offset
            if offset is None or offset == '':
                offset_value = 0
            else:
                offset_value = int(offset)

            if button_id == 'reset' or button_id == 'offset':
                return f"Current value: {offset_value}"

            if button_id == 'increment':
                if display is None or "Current value: " not in display:
                    current_value = 0
                else:
                    current_value = int(display.split(": ")[1])
                incremented_value = current_value + 1
                return f"Current value: {incremented_value}"

