import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.transpose(np.array(pd.read_csv("vaja4/podatki.csv")))


fig, ax = plt.subplots(1)
ax.plot(x[0],x[1], color="red")
ax.set_xlabel("Volumen [ccm]")
ax.set_ylabel("Tlak [kPa]")
ax.set_title("$p(V)$")
ax.fill_between(x[0], x[1], color="red")


plt.tight_layout()
plt.show()