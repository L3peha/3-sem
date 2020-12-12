import pandas as pd
import matplotlib.pyplot as plt

dec_info = pd.read_excel('students_info.xlsx')
results = pd.read_html('results_ejudge.html')[0]

df = results.merge(dec_info, left_on = 'User', right_on = 'login')

fig, ax = plt.subplots(2, 1)
df.groupby(['group_faculty'])['Solved'].mean().plot(kind='bar', title='Среднее кол-во решенных задач', ax=ax[0])
df.groupby(['group_out'])['Solved'].mean().plot(kind='bar', ax=ax[1])
print(df[(df.G>=10) | (df.H>=10)][['login','group_faculty','group_out']])
plt.show()