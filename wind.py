## Task 3

import plotly.express as px
import plotly.data as pldata

df = pldata.wind(return_type='pandas')

#print 1st and last 10 lines of df
print(df.head(10))
print(df.tail(10))

#group by strength to see how all strength categories
grouped = df.groupby("strength")
print(grouped.first())

#replace - with . and remove +
df['strength'] = df['strength'].str.replace("-", ".")
df['strength'] = df['strength'].str.replace("+", "")
print("df[strength]: \n", df['strength'])

#convert strength column to float
df['strength'] = df['strength'].astype(float)
df.info()

#make interactive scatterplot
wind_scatterplot = px.scatter(df, 
    x='strength', 
    y='frequency', 
    color='direction', 
    title='Wind Strength vs. Frequency', 
    hover_data=['frequency'], 
    labels={
        'strength': 'Strength'
        'frequency': 'Frequence'
    })
wind_scatterplot.write_html('wind.html', auto_open=True)
