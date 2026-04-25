import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("C:\\Users\\User\\Desktop\\Niru\\DAY4\\marks.csv")
print(df)

plt.bar(df["NAME"],df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks") 
plt.title("Student Marks Graph")
plt.show()


plt.pie(df["Marks"],labels=df["NAME"])
plt.title("Student Marks Distribution")
plt.show()

data=pd.read_csv("C:\\Users\\User\\Desktop\\Niru\\DAY4\\result.csv")
print(data)
plt.bar(data["Students"],data["TOTAL"])
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.title("Student Marks Graph")
plt.show()