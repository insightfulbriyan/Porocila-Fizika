import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from scipy.optimize import curve_fit


x = np.transpose(np.array(pd.read_csv("vaja1/vaja1-data.csv")))

time_limit = 2

nicle, _ = find_peaks(-np.abs(x[4]- np.mean(x[4][:495])))
# print(len(nicle))
# print(x[0][nicle[-1]] - x[0][nicle[0]])
frekvenca = (len(nicle)-2)/(2 * (x[0][nicle[-1]] - x[0][nicle[0]]))
# print(frekvenca)


peaks_x, _ = find_peaks(x[4]- np.mean(x[4][:495]))
peak_amplitudes_x = np.abs((x[4]- np.mean(x[4][:495]))[peaks_x])
amplituda_x = np.float32(np.mean(peak_amplitudes_x)) - 0.0225
# napaka_x = np.average(np.abs((x[4][:495] - np.mean(x[4][:495])) - amplituda_x*np.sin(2*np.pi*frekvenca*(x[0][:495] - 0.0852))))

peaks_v, _ = find_peaks(x[5]- np.mean(x[5][:495]))
peak_amplitudes_v = np.abs((x[5]- np.mean(x[5][:495]))[peaks_v])
amplituda_v = np.float32(np.mean(peak_amplitudes_v))
# napaka_v = np.average(np.abs((x[5][:495] - np.mean(x[5][:495])) - amplituda_v*np.sin(2*np.pi*frekvenca*(x[0][:495] - 0.7950530907))))
# napaka_v = np.average(np.abs((x[5][:495] - np.mean(x[5][:495])) - 2*np.pi*frekvenca*amplituda_x*np.sin(2*np.pi*frekvenca*(x[0][:495] - 0.7950530907))))

def dxdy(x, y = x[0], *, start=None, end=None):
    l = np.min([len(x), len(y)])
    return (np.diff(x[:l])/np.diff(y[:l]))[start:end]

# fig, ax = plt.subplots(3)
# ax[0].plot(x[0][:495], x[4][:495] - np.mean(x[4][:495]), label="2. poskus")
# ax[0].plot(x[0][:495], amplituda_x*np.sin(2*np.pi*frekvenca*(x[0][:495] - 0.0852)), label="best-fit")
# ax[0].set(xlim=(0, time_limit), ylim=(-0.5, 0.5), ylabel='odmik (m)', title="$s(t)$")
# ax[0].grid()


# ax[1].plot(x[0][:495], x[5][:495], label="2. poskus", color="blue")
# # ax[1].plot(x[0][:495], x[8][:495], label="3. poskus")
# ax[1].plot(x[0][:495], dxdy(amplituda_x*np.sin(2*np.pi*frekvenca*(x[0] - 0.0852)), end=495), label="odvod best-fit poti", color="orange")
# # ax[1].plot(x[0][:495], amplituda_v*np.sin(2*np.pi*frekvenca*(x[0][:495] - 0.7950530907)), label="3. poskus", color="green")
# ax[1].set(xlim=(0, time_limit), ylim=(-2, 2), ylabel='odmik (m)', title="$v(t)$")
# ax[1].grid()

# ax[2].plot(x[0][:495], x[6][:495], label="2. poskus", color="blue")
# # ax[2].plot(x[0][:495], dxdy(x[5], length=495), label="2. poskus", color="orange")
# ax[2].plot(x[0][:495], dxdy(dxdy(amplituda_x*np.sin(2*np.pi*frekvenca*(x[0] - 0.0852))), end=495), label="odvod best-fit hitrosti", color="green")
# # ax[2].plot(x[0][:495], np.diff(x[9])[:495]/np.diff(x[0])[:495], label="3. poskus")
# ax[2].set(xlim=(0, time_limit), ylim=(-20, 20), ylabel='odmik (m)', title="$v(t)$")
# ax[2].grid()
# ax[0].legend(loc="best")
# ax[1].legend(loc="best")
# sax[2].legend(loc="best")
# plt.tight_layout()
# plt.show()

print(f"Napaka v hitrosti {np.average(np.abs(dxdy(dxdy(amplituda_x*np.sin(2*np.pi*frekvenca*(x[0] - 0.0852))))[:495] - x[6][:495]))}" )


# # Function representing the displacement equation
# def displacement(t, A, omega, phi):
#     return A * np.cos(omega * t + phi)

# # Load your time, displacement data (adjust as needed)
# t_data = x[0]  # array of time values
# x_data = x[4] - np.mean(x[4])  # array of displacement values

# # Initial guess for the parameters (amplitude, angular frequency, phase)
# initial_guess = [np.max(x_data), 2 * np.pi * 1.0, 0]

# # Perform the curve fitting
# params, covariance = curve_fit(displacement, t_data, x_data, p0=initial_guess)

# # Extract the fitted parameters
# A_fit, omega_fit, phi_fit = params

# # Calculate estimated spring constant and mass
# k_estimated = omega_fit**2
# m_estimated = A_fit / k_estimated

# # Print the estimated values
# print("Estimated Spring Constant (k):", k_estimated)
# print("Estimated Mass (m):", m_estimated)

# # Plot the fit against the data (optional)
# plt.plot(t_data, x_data, label='Data')
# plt.plot(t_data, displacement(t_data, *params), label='Fit', linestyle='--')
# plt.legend()
# plt.show()
