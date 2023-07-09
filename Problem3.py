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