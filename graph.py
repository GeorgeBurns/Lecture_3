import matplotlib.pyplot as plt
import numpy as np


x = [i for i in range(0,6)]
y = [0,1,4,2,1,8]
z = [0,1,2,2,2,2]
plt.title("Confusion over time at uni")
plt.xlabel("Months")
plt.ylabel("Confusion")
plt.plot(x,y,z)
plt.legend(["George","Micky"])
plt.show()

