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

Students=["Arun","Bina","Chetan","Dviya","Esha"]
Marks=[75,85,90,70,95]
plt.bar(Students, Marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()

Students=["Arun","Bina","Chetan","Dviya","Esha"]
Marks=[75,85,90,70,95]
plt.plot(Students, Marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()

Students=["NIRU","DES","SAM","DITTU"]
Marks=[25,20,15,30]
plt.pie(Marks,labels=Students)
plt.title("Student Marks Distribution")
plt.show()