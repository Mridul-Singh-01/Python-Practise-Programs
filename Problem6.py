# Create the following NumPy arrays:
# a) A 1-D array called zeros having 10 elements and all the elements are set to zero.
# b) A 1-D array called vowels having the elements ‘a’, ‘e’, ‘i’, ‘o’ and ‘u’.
# c) A 2-D array called ones having 2 rows and 5 columns and all the elements are set to 1 and dtype as int.
# d) Use nested Python lists to create a 2-D array called myarray1 having 3 rows and 3 columns and store the following data: 2.7, -2, -19 0, 3.4, 99.9 10.6, 0, 13
# e) A 2-D array called myarray2 using arange() having 3 rows and 5 columns with start value = 4, step size 4 and dtype as float.

import numpy  as np
zeros = np.zeros((10,))
print (zeros)

vowels = np.array(list('aeiou'))
print (vowels)

ones =np.ones ((2,5),dtype=int)
print(ones )

myarray1  =np.array([[2.7,  -2,  -19],[0,  3.4,  99.9],[10.6,  0,  13]])
print (myarray1)

myarray2 = np.arange(4, 4+(3 * 5 * 4), 4 , dtype=float).reshape(3, 5)