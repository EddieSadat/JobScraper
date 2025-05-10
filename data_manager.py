# import pandas as pdg


# df = pd.read_csv("company_data.csv")

# print("This application manages the companies database.")
# print(df)

# action = input("\nAdd (A)   Modify (M)  Delete (D)  View (V):\n")

# if action == 'A':
#     name = input("Enter Company name: ")
#     url = input("Enter Company URL: ")

#     if
#     df = pd.concat([df,
#                     pd.DataFrame([[name, url]], columns=['Company', 'URL'])],
#                     ignore_index=True)
    
#     df.to_csv('company_data.csv')


import dash
from dash import dcc, html, dash_table, Input, Output, State
import pandas as pd

df = pd.read_csv('company_data.csv')


# Create the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Data Table', value='tab-1'),
        dcc.Tab(label='Untitled 2', value='tab-2')
    ]),
    html.Div(id='tabs-content')

])


# Callback to update content based on selected tab
@app.callback(
    Output('tabs-content', 'children'),
    Input('tabs', 'value')
)
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Content for Untitled 1'),
            html.P('This is the first tab.'),
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
                editable = True,
                row_deletable = True,
                style_table={'overflowX': 'auto'},
                page_size=5),
            html.Button('Add Row', id='add-row-button', n_clicks=0)
                ])
    
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Content for Untitled 2'),
            html.P('This is the second tab.')
        ])


@app.callback(
    Output('table', 'data'),
    Input('add-row-button', 'n_clicks'),
    # State('table', 'data')
)
def add_row(n_clicks, data):
    if n_clicks > 0:
        new_row = {col['id']: '' for col in [{"name": i, "id": i} for i in df.columns]}
        data.append(new_row)
    return data


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)