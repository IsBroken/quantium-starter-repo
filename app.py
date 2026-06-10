import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Create app
app = Dash(__name__)

app.layout = html.Div(

    style={
        "backgroundColor": "#f4f7fb",
        "padding": "30px",
        "fontFamily": "Arial"
    },

    children=[

        html.H1(
            "Soul Foods Pink Morsel Sales Dashboard",
            id ="header",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "30px"
            }
        ),

        html.Div(

            [

                html.H3(
                    "Select Region",
                    style={"color": "#34495e"}
                ),

                dcc.RadioItems(

                    id="region-picker",

                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],

                    value="all",

                    inline=True,

                    style={
                        "marginBottom": "25px",
                        "fontSize": "18px"
                    }

                ),

                dcc.Graph(id="sales-chart")

            ],

            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "12px",
                "boxShadow": "0px 2px 10px rgba(0,0,0,0.2)"
            }

        )

    ]

)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-picker", "value")
)

def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    sales = (
        filtered_df
        .groupby("date")["sales"]
        .sum()
        .reset_index()
        .sort_values("date")
    )

    fig = px.line(

        sales,

        x="date",
        y="sales",

        title="Pink Morsel Sales Over Time",

        labels={
            "date": "Date",
            "sales": "Sales"
        }

    )

    fig.add_vline(

        x="2021-01-15",

        line_dash="dash",
        line_color="red",

        annotation_text="Price Increase",

        annotation_position="top"

    )

    fig.update_layout(

        plot_bgcolor="white",

        paper_bgcolor="white",

        font=dict(size=16)

    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)