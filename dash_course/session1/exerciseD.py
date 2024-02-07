'''
Exercise D: using the following scatter plot example, add a scatter plot to your app that displays V (value/brightness) on the x-axis and S (saturation) on the y-axis.

Clue: to display the plot in the layout, remember to assign your plot to the figure property of the dcc.Graph, for example: dcc.Graph(figure=my_scatter_plot)
'''

from dash import Dash, html, dcc
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

shades = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')

scatter_fig = px.scatter(shades, x='V', y='L')

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
    html.Div([
        dcc.Dropdown(shades.brand.unique(), value='Revlon'),
        dcc.Input(id='input_number',
                  type='text',
                  placeholder='Input Hex Code')
    ]),
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
    ),
    dcc.Graph(figure=scatter_fig)
])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)