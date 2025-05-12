import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

# plot 1
plt.subplot(2,2,1)
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y = np.array([15,12,11,14,15,17,19,14,16,12,17,18])
plt.title("Spring",loc="left")
plt.xlabel("Week")
plt.ylabel("AVG Degree")
plt.plot(x,y)

# plot 2
plt.subplot(2,2,2)
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y = np.array([27,36,25,32,31,30,28,31,36,41,41,42])
plt.title("Summer",loc="left")
plt.xlabel("Week")
plt.ylabel("AVG Degree")
plt.plot(x,y)

# plot 3
plt.subplot(2,2,3)
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y = np.array([11,14,12,13,10,10,14,11,12,14,12,10])
plt.title("Fall",loc="left")
plt.xlabel("Week")
plt.ylabel("AVG Degree")
plt.plot(x,y)

# plot 4
plt.subplot(2,2,4)
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y = np.array([7,5,1,14,-1,-6,-3,8,9,-9,0,-1])
plt.title("Winter",loc="left")
plt.xlabel("Week")
plt.ylabel("AVG Degree")
plt.plot(x,y)

plt.show()