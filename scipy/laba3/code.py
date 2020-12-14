from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

y = Function('y')
y0 = sqrt(2)
x = symbols('x')
t = np.arange(0, 10, 0.1)

solve = dsolve(diff(y(x),x) + 2*y(x), 0, ics={y(0): y0})
print(solve)
solve1 = [solve.subs({x: xx}).rhs for xx in t]

def dydt(y, t):
	return -2*y

solve2 = odeint(dydt, y0, t)

y1 = np.array([float(x) for x in solve1])
y2 = np.array([float(x[0]) for x in solve2])

fig, ax = plt.subplots(1, 3)
ax[0].plot(t, solve1)
ax[1].plot(t, solve2)
ax[2].plot(t,y1-y2)
plt.show()