import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


# Calculating mean by formula
arr = np.array([4,5,2,8,5,9,3,1,9])
mean = np.sum(arr)/len(arr)
print(mean)


#importing data into dataframe
dataset = pd.read_csv('Titanic-Dataset.csv')

#Calculating average age from a data set using dataframe
print(f"Mean Age is {dataset['Age'].mean()} calculculated using Pandas")

#Calculating average age from a data set using Numpy 
print(f"Mean Age is {np.mean(dataset['Age'])} calculculated using Numpy")

#plotting 
sb.histplot(x ="Age",data=dataset,bins=[i for i  in range (0,81,10)])
plt.show()
