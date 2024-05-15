import dash
from dash import dcc, html
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
    html.H1("Sales Visualizer"),
    dcc.Graph(
        id='sales-chart',
        figure=px.line(df, x='Date', y='Sales', color='Region', title='Sales Data',
                       labels={'Sales': 'Total Sales', 'Date': 'Date'})
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
