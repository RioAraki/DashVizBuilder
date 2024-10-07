# Overview

The repo contains two modules:

1. dashVizBuilder

This is a svelte project which allows user to build Plotly Dash UI component in a graphic way.
After picking UI components and connect them with callback, save it in JSON.

2. dashCodeGen

This is a python project which transfers the json output from #1 to actual plotly dash code. The app boilerplate, complete layout and signature of the callback is generated for you. Only thing left is the body of the callback.

# TODO List

1. Reflect Graph's position and size to real UI layout
2. Make the default generated UI style much better by using tailwind 
3. Support graph and data table
4. Suport input group