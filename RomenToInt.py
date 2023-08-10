RomanNum=input("Enter the Roman Number : ")
RomanNum=list(RomanNum)
print(RomanNum)
VaidRoman=['I','V','X','L','C','D','M']
for i in range(0,len(RomanNum)):
    if RomanNum[i] in VaidRoman:
        f=1 
    else:
        f=0
        break
if(f==1):
    # ValueDic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    IntNum=[]
    sum=0
    c=0
    for i in range(0,len(RomanNum)):
        if RomanNum[i]=='I':
            IntNum.append(1)
        elif RomanNum[i]=='V':
            IntNum.append(5)
        elif RomanNum[i]=='X':
            IntNum.append(10)
        elif RomanNum[i]=='L':
            IntNum.append(50)
        elif RomanNum[i]=='C':
            IntNum.append(100)
        elif RomanNum[i]=='D':
            IntNum.append(500)
        elif RomanNum[i]=='M':
            IntNum.append(1000)
    for i in range(0,len(IntNum)):
        for j in range(i+2,len(IntNum)):
            if(IntNum[i]<IntNum[j]):
                c=1
                break
            
    if c!=1:
        for x in range(0,len(IntNum)):
            if x==(len(IntNum)-1):
                sum=sum+IntNum[x]
            elif IntNum[x]<IntNum[x+1]:
                sum=sum-IntNum[x]
            else:
                sum=sum+IntNum[x]
        print("Integer Number is : ",sum)
    else:
        print("Invalid Roman Number")
else:
    print("Invalid Input")