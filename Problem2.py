# Write a program to read a list of n integers (positive as well as negative).
# Create two new lists, one having all positive numbers and the other having all negative numbers from the given list. Print all three lists.

n=input("How many integers you want to enter in the list : ")
n=int(n)
int_list=[]
for i in range(n):
    integer=input("Enter the integer : ")
    int_list.append(int(integer))
print("\nAll Integer List")
print(int_list)
pos_int_list=[]
neg_int_list=[]
for i in range(n):
    if int_list[i]>=0:
        pos_int_list.append(int_list[i])
    else:
        neg_int_list.append(int_list[i])
        
print("\nPositive Integer List ")
print(pos_int_list)
print("\nNegative Integer List ")
print(neg_int_list)