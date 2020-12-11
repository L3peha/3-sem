import matplotlib.pyplot as plt
import numpy as np

f = open(input())
q = []
preps = [[],[],[],[],[],[],[]]
groups = [[],[],[],[],[],[]]
grad_pr = [[],[],[],[],[],[],[],[]]
grad_gr = [[],[],[],[],[],[],[],[]]
for line in f:
    q.append([n for n in line.split(';')])
grades = [3,4,5,6,7,8,9,10]
pr = set()
gr = set()
for elem in q:
    pr.add(elem[0])
    gr.add(elem[1])
grL = list(sorted(gr))
prL = list(sorted(pr))
for elem in q:
    for i in range(len(prL)):
        if elem[0]==prL[i]:
            preps[i].append(int(elem[2]))
    for i in range(len(grL)):
        if elem[1]==grL[i]:
            groups[i].append(int(elem[2]))

mas = np.zeros((len(prL),8))
mas2 = np.zeros((len(grL),8))
k=0
for i in preps:
    for j in range(len(i)):
        mas[k][i[j]-3] +=1
    k+=1
k=0
for i in groups:
    for j in range(len(i)):
        mas2[k][i[j]-3] +=1
    k+=1

fig1, ax1 = plt.subplots(2,len(prL))
for i in range(len(prL)):
        ax1[0][i].pie(mas[i], shadow=True, startangle=90)
        ax1[0][i].axis('equal')
        ax1[0][i].set_title(prL[i])
for i in range(len(grL)):
        ax1[1][i].pie(mas2[i], shadow=True, startangle=90)
        ax1[1][i].axis('equal') 
        ax1[1][i].set_title(grL[i])
ax1[1][len(grL)-1].legend(grades)
plt.show()
#I gave up trying to fix last one :((




