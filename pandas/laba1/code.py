import pandas as pd

df = pd.read_csv('transactions.csv')
print(df.loc[df['STATUS'] == 'OK'].sort_values(by='SUM', ascending=False).head(3))
print(df.loc[df['CONTRACTOR']=='Umbrella, Inc'].loc[df['STATUS'] == 'OK']['SUM'].sum())  #this one looks better for me than df.loc[(df["STATUS"] == "OK") & (df["CONTRACTOR"] == "Umbrella, Inc"), "SUM"].sum() ¯\_(ツ)_/¯
