n = int(input("Enter how many records you want to enter: "))
records={}
for i in range(n):
    name=input("Enter name of friend: ")
    number=input("Enter phone number: ")
    records[name]=number

while(True):
    print("Choose from the following options : ")
    print("1. Display the name and phone number of all your friends")
    print("2. Add a new key-value pair in this dictionary and display the modified dictionary")
    print("3. Delete a particular friend from the dictionary")
    print("4. Modify the phone number of an existing friend")
    print("5. Check if a friend is present in the dictionary or not")
    print("6. Display the dictionary in sorted order of names")
    print("7. Exit")
    c=int(input("Enter your choice : "))
    if c==1:
        print("\n",records,"\n")
    elif c==2:
        name=input("Enter name of friend: ")
        number=input("Enter phone number: ")
        records[name]=number
        print("\n",records,"\n")
    elif c==3:
        name=input("Enter name of friend: ")
        if name in records:
            del records[name]
            print("\n",records,"\n")
        else:
            print("\nNo such friend exists\n")
    elif c==4:
        name=input("Enter name of friend: ")
        if name in records:
            number=input("Enter phone number: ")
            records[name]=number
            print("\n",records,"\n")
        else:
            print("\nNo such friend exists\n")
    elif c==5:
        name=input("Enter name of friend: ")
        if name in records:
            print("\nYes friend is present in the record\n")
        else:
            print("\nNo friend is present in the record\n")
    elif c==6:
        print("\n",sorted(records),"\n")
    elif c==7:
        break
    else:
        print("\nInvalid choice\n")