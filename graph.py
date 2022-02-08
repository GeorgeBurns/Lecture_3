import matplotlib.pyplot as plt
import numpy as np


x = [i for i in range(0,6)]
y = [0,1,4,2,1,8]
plt.title("Confusion over time at uni")
plt.xlabel("Months")
plt.ylabel("Confusion")
plt.plot(x,y)
plt.show()

