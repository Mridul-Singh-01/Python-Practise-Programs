# Create the following Series and do the specified operations:
# a) EngAlph, having 26 elements with the alphabets as values and default index values.
# b) Vowels, having 5 elements with index labels ‘a’, ‘e’, ‘i’, ‘o’ and ‘u’ and all the five values set to zero. Check if it is an empty series.
# c) Friends, from a dictionary having roll numbers of five of your friends as data and their first name as keys.
# d) MTseries, an empty Series. Check if it is an empty series.
# e) MonthDays, from a numpy array having the number of days in the 12 months of a year. The labels should be the month numbers from 1 to 12.

import pandas as pd
import numpy as np
#a)
alpha=[chr(i) for i in range(97,123)]
EngAlph=pd.Series(alpha)
print(EngAlph)
#b)
vowels=pd.Series([0,0,0,0,0],index=['a','e','i','o','u'])
print(vowels)
if vowels.empty==True:
    print("Empty Series")
#c)    
Friends=pd.Series({'Rahul':'1','Rohit':'2','Raj':'3','Ravi':'4','Rajesh':'5'})
print(Friends)
#d)
MTseries=pd.Series([])
print(MTseries)
if MTseries.empty==True:
    print("Empty Series")
else:
    print("Not Empty Series")
#e)    
MonthDays=pd.Series(np.array([31,28,31,30,31,30,31,31,30,31,30,31]),index=[1,2,3,4,5,6,7,8,9,10,11,12])
print(MonthDays)
