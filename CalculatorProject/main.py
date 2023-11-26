inp=input("Please enter a number: ")
print("You entered:", inp)

number1=float(input("Enter first number: "))
op = input("Enter operator (+,-,*,/,^): ")
number2=float(input("Enter secont number"))
print(number1,op,number2)

def calculate(n1,n2,op):
    if op=="+":
        result=n1+n2
    elif op=="-":
        result=n1-n2
    elif op=="*":
        result=n1*n2
    elif op=="/":
        result=n1/n2
    elif op=="^":
        result=n1**n2

    return result
