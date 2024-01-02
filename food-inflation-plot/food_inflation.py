import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

inflation = pd.read_csv('food_inflation.csv')

fig, ax = plt.subplots()

plt.figure(figsize=(11,8))

plt.title('Food Inflation Over Time ', fontdict={'fontname':'Times New Roman','fontweight':'bold','fontsize':25})
# food inflation over time

for country in inflation:
  if country!='Year':
    plt.plot(inflation.Year, inflation[country], marker='.',label=country)

plt.xticks(inflation.Year[::1].tolist()+[2023]) #gas.Year[::3] may be deformed, thats why we make tolist()

plt.xlabel('Year', fontdict={'fontsize':15})
plt.ylabel('Inflation rate', fontdict={'fontsize':15})

plt.legend()


plt.savefig('food_inflation_figure.png',dpi=300)

plt.show()

