#install matplotlib, numpy, pandas libraries for this to work

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#lets plot
x = [0, 2, 4]
y = [0, 4, 8]
plt.plot(x,y)

#we can add a graph title this way
plt.title("My First Title", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})

#we can lable axis this way
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

#to show graph
plt.show()

