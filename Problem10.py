# Plot the following data using a line plot:
#    Day           1    2    3    4    5    6    7
# Tickets sold   2000 2800 3000 2500 2300 2500 1000

# a) Before displaying the plot display “Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday” in place of Day 1, 2, 3, 4, 5, 6, 7
# b)Change the color of the line to ‘Magenta’.

import matplotlib.pyplot as plt
Day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
Tickets_sold=[2000,2800,3000,2500,2300,2500,1000]
plt.plot(Day,Tickets_sold,color='magenta')
plt.xlabel('Day')
plt.ylabel('Tickets Sold')
plt.title('Tickets Sold Per Day')
plt.show()