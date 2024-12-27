import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

#importing data into dataframe
dataset = pd.read_csv("Titanic-Dataset.csv")


############# Range ################

min = dataset["Age"].min()
max  = dataset["Age"].max()
range = max - min 
#print(range)


####### Mean Absolute deviation #####
section_a = np.array([75,65,73,68,72,76])
section_b = np.array([90,47,43,96,93,51])
number = np.array([1,2,3,4,5,6])

# Mean is same for both data
mean = np.mean(section_a)

plt.figure(figsize=(10,3))
plt.scatter(section_a,number,color= "green",label="Section A")
plt.scatter(section_b,number,color= "red",label="Section B")
plt.plot([70,70,70,70,70,70],number,c="blue",label="Mean")
plt.legend()
plt.show()

# Using formula for mean absoulte devision of section a
mean_absoulte_devision_a =  np.sum(np.abs(section_a - mean))/len(section_a)
print(mean_absoulte_devision_a)


# Using formula for mean absoulte devision of section b
mean_absoulte_devision_b =  np.sum(np.abs(section_b - mean))/len(section_b)
print(mean_absoulte_devision_b)

