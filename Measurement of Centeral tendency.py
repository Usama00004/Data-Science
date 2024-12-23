import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


#################### MEAN ####################
# Calculating mean by formula
arr = np.array([4,5,2,8,5,9,3,1,9])
mean = np.sum(arr)/len(arr)
print(mean)

#importing data into dataframe
dataset = pd.read_csv("Titanic-Dataset.csv")

#Calculating mean age from a data set using dataframe
print(f"Mean Age is {dataset['Fare'].mean()} calculculated using Pandas")

#Calculating mean age from a data set using Numpy 
print(f"Mean Age is {np.mean(dataset['Fare'])} calculculated using Numpy")

#plotting 
mean = dataset["Fare"].mean()
# sb.histplot(x ="Age",data=dataset,bins=[i for i  in range (0,81,10)])
# plt.plot([mean for i in range(0,300)],[i for i in range (0,300)], c = "red")
# plt.show()


#################### MEDIAN ####################
dataset["Fare"].fillna(dataset["Fare"].mean(), inplace=True)
print(dataset.isnull().sum())

#Calculating median age from a data set using dataframe
print(f"Median Age is {dataset['Fare'].median()} calculculated using Pandas")

#Calculating mean age from a data set using Numpy 
print(f"Median Age is {np.median(dataset['Fare'])} calculculated using Numpy")

median = dataset["Fare"].median()
# sb.histplot(x ="Age",data=dataset,bins=[i for i  in range (0,81,10)])
# plt.plot([mean for i in range(0,300)],[i for i in range (0,300)], c = "red")
# plt.plot([median for i in range(0,300)],[i for i in range (0,300)], c = "blue")
# plt.show()

#################### MODE ####################
print("======Mode======")
print(dataset["Fare"].mode()[0])
print(dataset["Fare"].value_counts())

mode = dataset["Fare"].mode()[0]

sb.histplot(x ="Fare",data=dataset,bins=[i for i  in range (0,81,10)])
plt.plot([mean for i in range(0,300)],[i for i in range (0,300)], c = "red")
plt.plot([median for i in range(0,300)],[i for i in range (0,300)], c = "blue")
plt.plot([mode for i in range(0,300)],[i for i in range (0,300)], c = "green")

plt.show()


