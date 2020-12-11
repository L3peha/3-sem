import matplotlib.pyplot as plt
import matplotlib.animation as an

def axis(q):
    X = []
    Y = []
    for i in range(int(len(q))):
        if i % 2 == 0:
            X.append(max(q[i]))
            X.append(min(q[i]))
        else:
            Y.append(max(q[i]))
            Y.append(min(q[i]))
    return(min(X),max(X),min(Y) - 1,max(Y) + 1)

def plot(i):
    ax.clear()
    ax.grid()
    ax.axis(axis(q))
    line = ax.plot(q[i*2-2], q[i*2-1])
    return line

#-------------------------------------------------------------------
q=[]
f = open(input())   #frames.txt
for line in f:
    q.append([float(n) for n in line.split()])
fig, ax = plt.subplots()
if len(q)<30:
    fr = len(q) / 2
else:
    fr = 15

lab_animation = an.FuncAnimation(fig, plot, frames = int(len(q)/2), interval = 10, repeat = True)
lab_animation.save('gif.gif',fps = fr)


