import dash
from dash import dcc, html, callback_context
import pandas as pd
import plotly.express as px

# Read the formatted output CSV
df = pd.read_csv("formatted_output.csv")

# Sort dataframe by date
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

# Initialize Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1("Sales Visualizer", style={'text-align': 'center', 'color': '#333333'}),
    html.Div([
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'margin-right': '20px'}
        )
    ], style={'text-align': 'center'}),
    dcc.Graph(
        id='sales-chart',
        figure=px.line(df, x='Date', y='Sales', color='Region', title='Sales Data',
                       labels={'Sales': 'Total Sales', 'Date': 'Date'})
    )
])

# Define callback to update graph based on region selection
@app.callback(
    dash.dependencies.Output('sales-chart', 'figure'),
    [dash.dependencies.Input('region-filter', 'value')]
)
def update_figure(selected_region):
    filtered_df = df if selected_region == 'all' else df[df['Region'] == selected_region]
    fig = px.line(filtered_df, x='Date', y='Sales', color='Region', title='Sales Data',
                  labels={'Sales': 'Total Sales', 'Date': 'Date'})
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
