from dash import Dash, dcc, html, Input, Output, State, dash_table, callback
import pandas as pd

app = Dash(__name__, suppress_callback_exceptions=True)

df = pd.read_csv('company_data.csv')

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'backgroundColor': 'white'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

app.layout = html.Div([
    dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
        dcc.Tab(label='Data Table', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Tab 2', value='tab-2', style=tab_style, selected_style=tab_selected_style),
    ], style=tabs_styles),
    html.Div(id='tabs-content-inline'),
])

@callback(Output('tabs-content-inline', 'children'),
          Input('tabs-styled-with-inline', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1'),
            dash_table.DataTable(
                id='table',
                data=df.to_dict('records'),
                columns=[{"name": i, "id": i} for i in df.columns],
                style_cell={'textAlign': 'left'},
                style_header={'color': 'black',
                              'fontWeight':'bold',
                              'backgroundColor': 'rgb(210, 210, 210)'}, 
                editable = True,
                row_deletable = True,
                # style_table={'overflowX': 'auto'},
                page_size=1),
            html.Button('Add Row', id='add-row-button', n_clicks=0)
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])


@callback(
    Output('table', 'data'),
    Input('add-row-button', 'n_clicks'),
    State('table', 'data'),
    prevent_initial_call=True
)
def add_row(n_clicks, data):
    if n_clicks > 0:
        new_row = {col['id']: '' for col in [{"name": i, "id": i} for i in df.columns]}
        data.append(new_row)
    return data


if __name__ == '__main__':
    app.run(debug=True)