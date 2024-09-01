def generate_app():
    content = """
import dash
from layout import layout
from callback import register_callbacks_to_app

external_stylesheets = [
    "https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css"
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Set layout from layout.py
app.layout = layout

# Register callbacks
register_callbacks_to_app(app)


if __name__ == '__main__':
    app.run_server(debug=True)
"""
    with open("./output/app.py", "w") as file:
        file.write(content)
