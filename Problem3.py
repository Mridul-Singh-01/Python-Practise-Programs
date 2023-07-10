# Write a program to input names of n students and store them in a tuple. 
# Also, input a name from the user and find if this student is present in the tuple or not.

n=input("The number of records you want to enter : ")
n=int(n)
Student_name=[]
for i in range(n):
    name=input("Enter the name of student : ")
    Student_name.append(name)

Student_name=tuple(Student_name)
print(Student_name)
search_name=input("Enter the student name you want to search : ")
for i in range(n):
    if search_name==Student_name[i]:
        print("Student Name Found in the record ")
    else:
        print("Student Name not found in the record ")