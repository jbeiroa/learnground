'''
Exercise C: using the same shades.csv create a new app, where the layout has two new Dash Core Components that you haven’t used so far. --> Use a range slider for the L column.
'''

from dash import Dash, html, dcc
import dash_ag_grid as dag
import pandas as pd

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
] # there must be a way to make this without having to hardcode it

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Shades App'),
    html.Hr(),
    html.Div(
        dcc.Dropdown(shades.brand.unique(), value='Revlon')
    ),
    html.Div(
        dcc.RadioItems(shades_groups, inline=True)
    ),
    html.Div(
        dag.AgGrid(
            id='data_table',
            rowData=shades.to_dict('records'),
            columnDefs=[{'field': i} for i in shades.columns]
        )
    ),
    html.Div(
        dcc.RangeSlider(min=shades.L.min(),
                        max=shades.L.max(),
                        step=1,
                        count=1,
                        value=[shades.L.min(), shades.L.max()])
    )
])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)