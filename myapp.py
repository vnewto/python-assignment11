from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

#import gapminder dataset
countries_gdp = pldata.gapminder(return_type='pandas', datetimes=True)
print('countries_GDP data frame: \n', countries_gdp)

#create a series that has the list of countries
countries = countries_gdp['country'].drop_duplicates()
print('countries: ', countries)


# Initialize Dash app
app = Dash(__name__)
server = app.server

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth")
])

# Callback for dynamic updates
@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)

def update_graph(country):
    #filter dataframe so it only includes rows with that country name
    country_gdp = countries_gdp[countries_gdp['country'].str.contains(country)]
    #create line graph
    fig = px.line(country_gdp, x='year', y='gdpPercap', title=f"{country}'s GDP by Year")
    return fig

# Run the app
if __name__ == "__main__": 
    app.run(debug=True) 