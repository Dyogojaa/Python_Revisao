import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Create a data frame
df = pd.DataFrame({
    "Consumer Processing": [100, 200, 300],
    "Processing Atm": [400, 500, 600],
    "Processing Load": [700, 800, 900]
})

# Create a column chart
fig = px.bar(df, x="Processing Load", y="Consumer Processing")

# Create a list of inconsistencies
inconsistencies = [
    "Inconsistency 1",
    "Inconsistency 2",
    "Inconsistency 3"
]

# Create a dashboard
app = dash.Dash()

# Add the column chart
app.layout = html.Div([
    dcc.Graph(figure=fig),
    html.H3("List of Inconsistencies"),
    dcc.List(children=inconsistencies)
])

# Run the dashboard
app.run_server()