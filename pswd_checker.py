def pswd_checker(input_str):
    n=len(st)
    LOW=False
    HIGH=False
    SPL=False
    DIGIT=False
    for i in range(n):
        if input_str[i].islower():
            LOW = True
        elif input_str[i].isupper():
            HIGH= True
        elif input_str[i].isdigit():
            DIGIT=True
        elif not input_str[i].isalnum():
            SPL=True
    return LOW,HIGH,SPL,DIGIT,n

st=input("Enter the string: ")
LOW,HIGH,SPL,DIGIT,n=pswd_checker(st)

print("Password complexity: ")
if(n>=8 and LOW and  HIGH and  SPL and DIGIT):
    print('Strong ')
elif(n>=6 and ((LOW and  HIGH) or  SPL or DIGIT)):
    print('Medium ')
else:
    print('Weak')