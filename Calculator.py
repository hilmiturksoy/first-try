from win32cryptcon import dwFORCE_KEY_PROTECTION_USER_SELECT


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "Error: Division by zero"
    return a/b

def calculator():
        while True:
            print("Select operation.")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")
            print("5.Exit")

            try:
                choice = int(input("Enter choice(1/2/3/4/5): "))
            except ValueError:
                print("Invalid input")
                continue
            if choice == 5:
                print("Exiting...")
                break
            if not choice in [1,2,3,4]:
                print("Please choice 1,2,3,4")
                continue
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input")
                continue
            if choice == 1:
                print(f"{num1} + {num2} = {add(num1,num2)}")
            elif choice == 2:
                print(f"{num1} - {num2} = {sub(num1,num2)}")
            elif choice == 3:
                print(f"{num1} * {num2} = {mul(num1,num2)}")
            elif choice == 4:
                print(f"{num1} / {num2} = {div(num1,num2)}")



calculator()