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
print(f"Mean Age is {dataset['Age'].mean()} calculculated using Pandas")

#Calculating mean age from a data set using Numpy 
print(f"Mean Age is {np.mean(dataset['Age'])} calculculated using Numpy")

#plotting 
mean = dataset["Age"].mean()
# sb.histplot(x ="Age",data=dataset,bins=[i for i  in range (0,81,10)])
# plt.plot([mean for i in range(0,300)],[i for i in range (0,300)], c = "red")
# plt.show()


#################### MEDIAN ####################
dataset["Age"].fillna(dataset["Age"].mean(), inplace=True)
print(dataset.isnull().sum())

#Calculating median age from a data set using dataframe
print(f"Median Age is {dataset['Age'].median()} calculculated using Pandas")

#Calculating mean age from a data set using Numpy 
print(f"Median Age is {np.median(dataset['Age'])} calculculated using Numpy")

mode = dataset["Age"].median()
# sb.histplot(x ="Age",data=dataset,bins=[i for i  in range (0,81,10)])
# plt.plot([mean for i in range(0,300)],[i for i in range (0,300)], c = "red")
# plt.plot([mode for i in range(0,300)],[i for i in range (0,300)], c = "blue")
# plt.show()



