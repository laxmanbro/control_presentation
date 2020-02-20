from scipy import signal
import matplotlib.pyplot as plt
s1 = signal.TransferFunction([1], [1, 3 ,2]) # TF = 1/(s^2+3s+2)


w, mag, phase = signal.bode(s1)

plt.figure()
plt.title('magnitude plot')
plt.xlabel('frequency rad/s')
plt.ylabel('magnitude dB')
plt.semilogx(w, mag)    
# plt.grid()

plt.figure()
plt.title('phase plot')
plt.xlabel('frequency rad/s')
plt.semilogx(w, phase)  
# plt.grid()
plt.ylabel('phase deg')
plt.show()