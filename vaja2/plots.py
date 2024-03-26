import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

N = 0  # st poskusa 0, 1, 2; 0 je najbolj točen
x = np.transpose(np.array(pd.read_csv("vaja2/podatki.csv")))

cas = []
pot = []

pot_cnt = 0
for i in range(len(x[1])):
    if x[1 + N*2][i] == 1:
        pot.append(pot_cnt)
        pot_cnt += 0.01  # razmak med črticami
        # popravek da je začetni čas 0
        cas.append(x[0 + N*2][i] - x[0 + N*2][1])

cas = np.array(cas)
pot = np.array(pot)

hitrost = np.diff(pot)/np.diff(cas)  # odvod poti
pospesek = np.diff(hitrost)/np.diff(cas)[1:]  # odvod hitrosti

acc = np.average(pospesek)

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
ax[0].plot(cas[1:13], pot[:12], label="Pot", color="red")
ax[0].set_xlabel("čas [s]")
ax[0].set_ylabel("Pot [m]")
ax[0].set_title("Pot in hitrost - izmrjena")
ax2 = ax[0].twinx()
ax2.plot(cas[1:13], hitrost[:12], label="Hitrost", color="blue")
ax2.set_ylabel("Hitrost [$\\frac{\\text{m}}{\\text{s}}$]")
ax[0].grid()


ax[1].plot(cas[1:13], dis[:12], label="Pot - izračunana", color="violet")
ax[1].set_xlabel("čas [s]")
ax[1].set_ylabel("Pot [m]")
ax[1].set_title("Pot in hitrost - izračunana")
ax2 = ax[1].twinx()
ax2.plot(cas[1:13], vel[:12], label="Hitrost - izračunana", color="green")
ax2.set_ylabel("Hitrost [$\\frac{\\text{m}}{\\text{s}}$]")
ax[1].grid()
plt.tight_layout()
plt.show()