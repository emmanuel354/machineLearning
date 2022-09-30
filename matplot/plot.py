#install matplotlib, numpy, pandas libraries for this to work

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#resize graph
plt.figure(figsize=(5,3), dpi=100)

#lets plot
x = [0, 2, 4]
y = [0, 4, 8]
plt.plot(x,y, label="y=2x", color='red', linewidth=2, marker='.', markersize=10, markeredgecolor='black')

#adding legend which is possible by adding label="your legend" command prior
plt.legend()

#we can add a graph title this way
plt.title("My First Title", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})

#we can lable axis this way
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

#we can use numpy for our arrays
x2 = np.arange(0,4.5,0.5)
plt.plot(x2, x2**2, 'b', label='x^2')
plt.legend()

plt.savefig("./graphs/mygraph1.png")


#to show graph
#plt.show()
