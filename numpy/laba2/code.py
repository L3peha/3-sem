import numpy as np
import matplotlib.pyplot as plt

mas = np.loadtxt(input())
clear = []
for i in range(mas.size):
    if i<9:
        clear.append(mas[:i+1].mean())
    else:
        clear.append(mas[i-9:i].mean())
clear = np.array(clear)
plt.plot(clear)
plt.show()

fig, ax = plt.subplots(1,2)
ax[0].plot(mas)
ax[0].set_title('Сырой сигнал')
ax[0].grid()
ax[1].plot(clear)
ax[1].set_title('После фильтра')
ax[1].grid()
plt.show()


