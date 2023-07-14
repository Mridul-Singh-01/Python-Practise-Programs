# Use the DataFrame created in Problem 2 above to do the following:
# a) Display the row labels of Sales.
# b) Display the column labels of Sales.
# c) Display the data types of each column of Sales.
# d) Display the dimensions, shape, size and values of Sales.
# e) Display the last two rows of Sales.
# f) Display the first two columns of Sales.

import pandas as pd

data=pd.DataFrame({'2014':[100.5,150.8,200.9,30000,40000],'2015':[12000,18000,22000,30000,45000],'2016':[20000,50000,70000,100000,125000],'2017':[50000,60000,70000,80000,90000]},index=['Madhu','Kusum','Kinshuk','Ankit','Shruti'])
print(data)
#a)
print("\nRow Labels of Sales")
print(data.index)
#b)
print("\nColumn Labels of Sales")
print(data.columns)
#c)
print("\nData Types of each column of Sales")
print(data.dtypes)
#d)
print("\nDimensions of Sales")
print(data.ndim)
print("\nShape of Sales")
print(data.shape)
print("\nSize of Sales")
print(data.size)
print("\nValues of Sales")
print(data.values)
#e)
print("\nLast two rows of Sales")
print(data.tail(2))
#f)
print("\nFirst two columns of Sales")
print(data.iloc[:,0:2])
