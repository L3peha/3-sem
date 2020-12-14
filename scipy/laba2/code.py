from scipy import linalg
import matplotlib.pyplot as plt

with open(f"{input()}") as f:
    lines = f.readlines()
#print(lines)
lines = [list(map(float, line.strip().split())) for line in lines]
#print(lines)
N = int(lines[0][0])
A = lines[1:N+1]
b = lines[N+1]
y = linalg.solve(A,b)

fig, ax = plt.subplots()
ax.bar(range(len(y)), y)
ax.set(xlabel="Номер решения")
plt.grid()
plt.show()