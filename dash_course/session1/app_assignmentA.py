'''
1. A Dropdown that uses the column brand as the dropdown options. Make sure the brand names are unique (do not repeat themselves). Then, assign “Revlon” as the initial value.

2. A RadioItems component in which the values from the column named group are assigned to the options property. The options should be unique and sorted from 0 to 7.

3. Update the options property of the RadioItems component so that the values (of the options) represent numbers from 0 to 7, but the labels are their respective strings (see Readme-shades for the strings).
'''

from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

shades = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')

shades_groups = [
    {'label': 'Fenty Beauty\'s PRO FILT\'R Foundation Only',
    'value': 0},
    {'label': 'Make Up For Ever\'s Ultra HD Foundation Only',
    'value': 1},
    {'label': 'US Best Sellers',
    'value': 2},
    {'label': 'BIPOC-recommended Brands with BIPOC Founders',
    'value': 3},
    {'label': 'BIPOC-recommended Brands with White Founders',
    'value': 4},
    {'label':'Nigerian Best Sellers',
    'value': 5},
    {'label': 'Japanese Best Sellers',
    'value': 6},
    {'label': 'Indian Best Sellers',
    'value': 7}
]

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Shades App'),
    html.Hr(),
    html.Div(
        dcc.Dropdown(shades.brand.unique(), value='Revlon')
    ),
    html.Div(
        dcc.RadioItems(shades_groups)
    )
])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)