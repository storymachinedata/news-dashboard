import dash
#import dash_core_components as dcc 
from dash import dcc
#import dash_html_components as html
from dash import html
from dash.dependencies import Input, Output, State
from pull_news2 import get_news
from dash.exceptions import PreventUpdate
import os

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
server = app.server


app = dash.Dash()

app.layout = html.Div([
    dcc.Input(
        id="query_string",
        placeholder="Choose a country",
        type="text"
    ),
    html.Button("Search", id="search_button"),
    html.Div(id="content")
])

@app.callback(
    Output("content", "children"),
    [Input("search_button", "n_clicks")],
    [State("query_string", "value")]
)

def get_news_callback(v, q):
    if v!= None:
        news = get_news(q)
    else:
        raise PreventUpdate

    html_string = []

    for n in news:
        html_string.append(
            html.Div([
                html.H1([n[0]], className="title"),
                html.P(n[1], className="p" ),
                html.P(n[2]),
                html.P(n[3])
            ])
        )

    return html_string
    

#app.run_server(debug=True)

if __name__ == "__main__":
    app.run_server(debug=True)
