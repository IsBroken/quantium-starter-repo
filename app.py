import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load the processed data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Group sales by date
daily_sales = df.groupby("date")["sales"].sum().reset_index()

# Create the line chart
fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Sales"
    }
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([

    html.H1(
        "Soul Foods Pink Morsel Sales Visualiser",
        style={"textAlign": "center"}
    ),

    dcc.Graph(
        figure=fig
    )

])

if __name__ == "__main__":
    app.run(debug=True)