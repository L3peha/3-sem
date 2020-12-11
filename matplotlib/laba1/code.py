import matplotlib.pyplot as plt

n = [str(s) for s in input().split()]     #001.dat 002.dat 003.dat 004.dat
x = []
y = []
for i in range(int(len(n))):
    f = open(n[i],'r')
    num = int(f.readline().split()[0])
    for line in f:
        q = [float(n) for n in line.split()]
        x.append(q[0])
        y.append(q[1])
        num -=1
        if num==0:
            break
    plt.plot(x, y,marker ='o',linestyle=' ',color='black')
    kx = (max(x)- min(x))/10
    ky = (max(y)- min(y))/10
    plt.axis([min(x) - kx, max(x) + kx, min(y)-ky, max(y)+ky])
    plt.title("Number of points" + ": " + str(len(x)))
    plt.show()
    f.close      #rn new graph aft closing prev, will try to fix it

