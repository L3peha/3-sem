import numpy as np
import matplotlib.pyplot as plt

f = open(input())
N = int(f.readline())
x = np.arange(N)
arr = np.loadtxt(f)
b = arr[N]
A = arr[0:N].reshape(N,N)
y = np.linalg.solve(A,b) #i try to solve by sympy, but it was hard to make matrix(N,N+1) from matrix0(N+1,N) where
                         #matrix0[N+1][from 0 to N] = b (we need matrix[i][N+1]=matrix[N+1][i] to use linsolve(system,...), so i use np
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set(xlabel="Номер решения")
plt.grid()
plt.show()