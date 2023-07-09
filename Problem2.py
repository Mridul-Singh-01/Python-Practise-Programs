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