# Use company_sales_data.csv file from github folder to solve these questions.
# Get total profit of all months and show line plot with the following Style properties

import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_csv('company_sales_data.csv')
print(data)
profit=data['total_profit'].sum()
print("Total profit of all months : ",profit)
