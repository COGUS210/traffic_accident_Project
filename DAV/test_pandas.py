import pandas as pd
from pandas import DataFrame
from pandas import Series
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

text = pd.read_csv("sample.csv",
                   sep = ",",
                   names = ['date', 'total', 'death', 'injuries'],
                   converters = {'date': str },
                   header = None)

text['date'] = pd.to_datetime(text['date'])
#print(text)
grouped = text.groupby(text['date'].dt.strftime('%Y'))['death'].sum()

gdf = pd.DataFrame({'date': grouped.index.astype(int), 'death': grouped.values})
x = gdf.iloc[:, 0].values
y = gdf.iloc[:, 1].values.reshape(-1, 1)
z = np.array([2018, 2019, 2020, 2021, 2022, 2023])
z = np.append(x, z)
predz = z.reshape(-1, 1)
x = x.reshape(-1, 1)

lin_reg = LinearRegression()
lin_reg.fit(x, y)
def viz_linear():
    plt.scatter(x, y, color='red')
    plt.plot(predz, lin_reg.predict(predz), color='blue')
    plt.xticks(z)
    plt.title("Yearly Accident Changes")
    plt.xlabel("Year")
    plt.ylabel("Total Death Accident Numbers")
    plt.show()
    return
viz_linear()