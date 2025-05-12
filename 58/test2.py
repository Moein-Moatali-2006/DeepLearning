import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,10,14,17,35,12,17,12]) ** 1.5
y = np.array([14,18,20,21,26,27,35,40]) ** 1.5
plt.scatter(x,y,color="red")

x = np.array([5,10,14,17,35,12,17,12]) ** 2 
y = np.array([14,18,20,21,26,27,35,40]) ** 2 
plt.scatter(x,y,color="green")


plt.show()