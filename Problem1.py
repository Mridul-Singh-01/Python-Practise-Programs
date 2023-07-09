text=input("Enter the text :")
print("\n")
print("Entered text is : ",text)
print("The total number of characters in the text : ", len(text))
Alpha_sum=0
for c in text:
    if c.isalpha():
        Alpha_sum=Alpha_sum+1
    
print("The total number of alphabets in the text : ",Alpha_sum)
Digit_sum=0
for c in text:
    if c.isdigit():
        Digit_sum=Digit_sum+1
        
print("The total number of digits in the text : ",Digit_sum)
Special_sym_sum=0
for c in text:
        if not (c.isalpha() or c.isdigit() or c == ' '):
            Special_sym_sum=Special_sym_sum+1
            
print("The total number of special symbols in the text : ",Special_sym_sum)
x=text.split()

print("The total number of words in the given text : ",len(x))