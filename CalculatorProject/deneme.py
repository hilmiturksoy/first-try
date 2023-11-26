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


def main():
    while True:
        try:
            number1 = float(input('Enter first number: '))
            op = input('Enter operator (+, -, *, /, **): ')
            number2 = float(input('Enter second number: '))


            result = calculate(number1, number2, op)
            print("sonuç", result)

        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

        except ZeroDivisionError:
            print("Error: Division by zero.")

        except Exception as hata:
            print(f"An error occurred: {hata}")

        devam_et = input("Devam etmek istiyormusunuz? (evet/hayır): ")
        if devam_et.lower() != 'evet':

            break


if __name__ == "__main__":
    main()