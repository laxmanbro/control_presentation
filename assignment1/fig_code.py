from scipy import signal
import matplotlib.pyplot as plt
s1 = signal.lti([1], [1, 2, 3])
s2 = signal.lti([1, 1], [1, 4, 6, 4])
w, mag, phase = signal.bode(s1)
hh, mag, phase = signal.bode(s2)

plt.figure()
plt.semilogx(w, mag)    # Bode magnitude plot
plt.semilogx(hh, mag)

# plt.figure()
# plt.semilogx(w, phase)  # Bode phase plot
plt.show()
