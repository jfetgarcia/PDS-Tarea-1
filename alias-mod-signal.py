
from enum import Enum
import matplotlib.pyplot as plt
import numpy as np
import os


f_mod = 1000
f_inf = 100
f_sig1 = 900
f_sig2 = 1100

f_samp = f_mod

num_cycle = 3

# Calculating for x(t)
time_shown = (1/f_inf) * num_cycle

time = np.linspace(0, time_shown, 10000)

x_t = np.cos(2*np.pi*f_mod*time) \
        + 0.25*np.cos(2*np.pi*f_sig1*time) \
        + 0.25*np.cos(2*np.pi*f_sig2*time)

# Sampled sine wave
x_n_sample =  np.arange(0, time_shown, 1/f_samp)

x_n = np.cos(2*np.pi*f_mod*x_n_sample) \
        + 0.25*np.cos(2*np.pi*f_sig1*x_n_sample) \
        + 0.25*np.cos(2*np.pi*f_sig2*x_n_sample)

# Calculating for m(t)
time_shown_m = (1/f_inf) * num_cycle
time_m = np.linspace(0, time_shown_m, 10000)
m_t = np.cos(2*np.pi*f_inf*time_m)

# Apply operations which should allow to get 
# m(n) values correctly
m_n = 2*(x_n-1)

print("Values of m[n]")
print(m_n)
print("Values of x[n]")
print(x_n)

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

ax1.set_title('Plot of x(t)')
ax1.set_xlabel('t(s)')
ax1.set_ylabel('Amplitude')


ax1.plot(time, x_t, label="x(t)", color="blue", linewidth=2)
ax1.scatter(x_n_sample, x_n, label="x[n]", color="red")
ax1.vlines(x_n_sample, ymin=0, ymax=x_n, colors='red', linestyles='dashed')
ax1.legend()


ax2.set_title('Plot of m(t)')
ax2.set_xlabel('t(s)')
ax2.set_ylabel('Amplitude')


ax2.plot(time_m, m_t, label="m(t)", color="blue", linewidth=2)
ax2.scatter(x_n_sample, m_n, label="m[n]", color="red")
ax2.vlines(x_n_sample, ymin=0, ymax=m_n, colors='red', linestyles='dashed')
ax2.legend()

plt.show()