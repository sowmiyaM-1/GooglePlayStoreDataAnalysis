

#Create a scatter plot to visualize the relationship between revenue and the number of installs for paid apps only.
#Add a trendline to show the correlation and color-code the points based on app categories.


import pandas as pd
import plotly.express as px

data = pd.read_csv('C:/Users/sowmi/OneDrive/Documents/AI/Nullclass/Play Store Data.csv')

data = data[data['Type'] == 'Paid']

data['Price'] = data['Price'].apply(lambda x: str(x).replace('$', '') if isinstance(x, str) else x).astype(float)

data['Installs'] = data['Installs'].str.replace(r'[^\d]', '', regex=True).astype(int)


data['Revenue'] = data['Price'] * data['Installs']


data = data[['Category', 'Price', 'Installs', 'Revenue']]

fig = px.scatter(
    data,
    x='Installs',
    y='Revenue',
    color='Category',
    title='Revenue vs Installs with App Categy',
    labels={'Installs': 'Number of Installs', 'Revenue': 'Revenue ($)'},
    hover_data=['Price'],
    template='plotly'
)

fig = px.scatter(
    data,
    x='Installs',
    y='Revenue',
    color='Category',
    trendline='ols',
    title='Revenue vs Installs with App Category',
    labels={'Installs': 'Number of Installs', 'Revenue': 'Revenue ($)'},
    hover_data=['Price'],
    template='plotly'
)

fig.show()
fig.write_html('dashboard1.html')