import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax = plt.axes(xlim=(0, 50), ylim=(0, 10))
ax.grid()

data0 = np.genfromtxt('start.txt')
data = data0
line, = ax.plot([], [])

A = np.eye(50) - np.roll(np.eye(50), -1, axis=1)

def animate(i):
    global data
    if i == 0:
        data = data0
    else:
        data = data - 0.5 * A @ data
    X = np.arange(50)
    line.set_data(X, data)  # update the data.
    return line,

ani = animation.FuncAnimation(fig, animate, frames=255, interval=0, repeat = True)
ani.save('numpyGif.gif',fps=20)