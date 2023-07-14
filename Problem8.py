# Create the following DataFrame Sales containing year wise sales figures for five sales persons in INR. 
# Use the years as column labels, and sales person names as row labels
#          2014  2015  2016  2017
# Madhu   100.5 12000 20000 50000
# Kusum   150.8 18000 50000 60000
# Kinshuk 200.9 22000 70000 70000
# Ankit   30000 30000 100000 80000
# Shruti  40000 45000 125000 90000

import pandas as pd

data=pd.DataFrame({'2014':[100.5,150.8,200.9,30000,40000],'2015':[12000,18000,22000,30000,45000],'2016':[20000,50000,70000,100000,125000],'2017':[50000,60000,70000,80000,90000]},index=['Madhu','Kusum','Kinshuk','Ankit','Shruti'])
print(data)
