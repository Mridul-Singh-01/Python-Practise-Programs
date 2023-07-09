n=input("The elements you wnat to enter : ")
n=int(n)
List=[]
for i in range(n):
    element=int(input("Enter the element : "))
    List.append(element)
print("Entered List is : ")
print(List)
unique_list=[]
for i  in List:
    if i not in unique_list:
        unique_list.append(i)
print("List of Unique elements is : ")
print(unique_list)
        