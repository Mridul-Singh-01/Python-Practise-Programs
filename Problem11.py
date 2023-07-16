# Use company_sales_data.csv file from github folder to solve these questions.
# Get total profit of all months and show line plot with the following Style properties
# Line Style dotted and Line-color should be red
# Show legend at the lower right location.
# X label name = Month Number
# Y label name = Sold units number
# Add a circle marker.
# Line marker color as read
# Line width should be 3

import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_csv('company_sales_data.csv')
print(data)
profit=data['total_profit'].sum()
print("Total profit of all months : ",profit)
month=data['month_number'].tolist()
sold=data['total_units'].tolist()
plt.plot(month,sold,'r--',linewidth=3,marker='o',markerfacecolor='r',markersize=12)
plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.legend(loc='lower right')
plt.title('Company Sales data of last year')
plt.show()
