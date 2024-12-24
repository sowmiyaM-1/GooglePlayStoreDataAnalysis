import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


data = pd.read_csv('Play Store Data.csv')


# 1. Filtered only paid apps
data = data[data['Type'] == 'Paid']

# 2. Handling of strings like $ in the price column 
data['Price'] = data['Price'].apply(lambda x: str(x).replace('$', '') if isinstance(x, str) else x).astype(float)

# 3. Handling of the characters like + into int
data['Installs'] = data['Installs'].str.replace(r'[^\d]', '', regex=True).astype(int)

# 4. calculate revenue= Price* Installs to show the scatterplot
data['Revenue'] = data['Price'] * data['Installs']

# 5. Change the data frame based on our need 
data = data[['Category', 'Price', 'Installs', 'Revenue']]

# 6. Scatterplot of Revenue vs Installs 
plt.figure(figsize=(10, 10))
sns.scatterplot(
    data=data,
    x='Installs',
    y='Revenue',
    hue='Category',
    palette='viridis',
    s=100
)

# 7. Trendline for correlation
z = np.polyfit(data['Installs'], data['Revenue'], 1)  # Linear fit
p = np.poly1d(z)
plt.plot(data['Installs'], p(data['Installs']), color='red', linestyle='--', label='Trendline')



plt.title('Revenue vs Installs with App Category', fontsize=14)
plt.xlabel('Number of Installs', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)

plt.legend(
    title='App Category',
    fontsize=12,
    title_fontsize=12,
    bbox_to_anchor=(1.05, 1), 
    loc='upper left'
)

plt.grid(True)
plt.show()



