import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('flights.csv')
fig, ax = plt.subplots(1,3)
df.groupby('CARGO').size().plot(kind='bar', title='Number of flights', ax=ax[0])
df.groupby('CARGO')['WEIGHT'].sum().plot(kind='bar', title='Total weight', ax=ax[1])
df.groupby('CARGO')['PRICE'].sum().plot(kind='bar', title='Total price', ax=ax[2])
plt.show()