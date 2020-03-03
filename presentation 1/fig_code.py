from scipy import signal
import matplotlib.pyplot as plt
s1 = signal.TransferFunction([1], [1, 3, 2])  # TF = 1/(s^2+3s+2)
s2 = signal.TransferFunction([1], [1, 4, 6, 4])  # TF = 1/(s^3+4s^2+6s+4)


w, mag, phase = signal.bode(s1)
h, mag, phase = signal.bode(s2)

plt.figure()
plt.title('magnitude plot')
plt.xlabel('frequency rad/s')
plt.ylabel('magnitude dB')
plt.semilogx(w, mag)
plt.semilogx(h, mag)

# plt.grid()

# plt.figure()
# plt.title('phase plot')
# plt.xlabel('frequency rad/s')
# plt.semilogx(h, mag)
# # plt.grid()
# plt.ylabel('phase deg')


plt.show()
