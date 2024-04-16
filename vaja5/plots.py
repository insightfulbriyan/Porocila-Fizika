import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.transpose(np.array(pd.read_csv("vaja5/podatki.csv")))


cas = []
pot = []
pot_cnt = 0
for i in range(len(x[1])):
    if x[1][i] == 1:
        pot.append(pot_cnt)
        pot_cnt += 0.015  # razmak med črticami
        # popravek da je začetni čas 0
        cas.append(x[0][i] - x[0][2])

cas = np.array(cas)
pot = np.array(pot)

hitrost = np.diff(pot)/np.diff(cas)  # odvod poti
pospesek = np.diff(hitrost)/np.diff(cas)[1:]  # odvod hitrosti

acc = np.average(pospesek[:30])
print(acc)
print(np.sort(np.abs(acc-pospesek[:30]))[20])

vel = []
v = hitrost[0]
for i in range(len(cas)-1):
    vel.append(v)
    v += acc*np.diff(cas)[i]

dis = []
d = 0
for i in range(len(cas)-1):
    dis.append(d)
    d += vel[i]*np.diff(cas)[i]

fig, ax = plt.subplots(2)
ax[0].plot(cas[2:32], pot[:30], label="Pot", color="red")
ax[0].set_xlabel("čas [s]")
ax[0].set_ylabel("Pot [m]")
ax[0].set_title("Pot in hitrost - izmrjena")
ax2 = ax[0].twinx()
ax2.plot(cas[2:32], hitrost[:30], label="Hitrost", color="blue")
ax2.set_ylabel("Hitrost [$\\frac{\\text{m}}{\\text{s}^2}$]")
ax3 = ax[0].twinx()
ax2.plot(cas[2:32], pospesek[:30], label="Pospesek", color="green")
ax2.set_ylabel("Pospesek [$\\frac{\\text{m}}{\\text{s}^2}$]")
ax[0].grid()

plt.tight_layout()
plt.show()