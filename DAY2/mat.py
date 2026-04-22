import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([10,20,70,200])
ypoints = np.array([20,30,150,200])

#plot line with markers
plt.plot(xpoints,ypoints,marker='o')

#add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("simple line graph")

#show grid
plt.grid()
#display the graph
plt.show()

