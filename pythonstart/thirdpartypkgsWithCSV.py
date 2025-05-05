import pandas as pd
import matplotlib.pyplot as plt 

file = "data.csv"  # data file conetains numbers and years of any objest.


data = pd.read_csv(file)
print(data)
print("------")
print(data(data["X"]>=10000)) 
print(data(data["Y"]==2015)) 

# Scatter graph for Car X VS Y 
plt.scatter(data["Y"],data["X"])

plt.title("X VS Y")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
