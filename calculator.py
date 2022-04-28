def main():
    print("Welcome to the calculator")
    print("What do you wish to do?")
    print("1. Addition")
    print("2. Sustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponential")
    print("6. Module")
    print("7. Comparison")
    print("8. Absolute value")
    choice=int(input("Enter your choice:"))
    if choice==1:
        suma()
    elif choice==2:
        resta()
    elif choice==3:
        multiplicacion()
    elif choice==4:
        division()
    elif choice==5:
        potencia()
    elif choice==6:
        modulo()
    elif choice==7:
        comparacion()
    elif choice==8:
        valor_absoluto()

def suma():
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    result=num1 + num2
    print("The result is",result)
def resta():
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    result=num1 - num2
    print("The result is",result)
def multiplicacion():
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    result=num1 * num2
    print("The result is",result)
def division():
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    if num2!=0:
        result=num1 / num2
        print("The result is",result)
    else:
        print("You cant divide by 0")
def potencia():
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    result=num1 ** num2
    print("The result is",result)
def modulo():
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    result=num1 % num2
    print("The result is",result)
def comparacion():
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    if num1>num2:
        print(num1, "es mayor que", num2)
    else:
        print(num2, "es mayor que", num1)
def valor_absoluto():
    num1=int(input("Enter a number:"))
    print(abs(num1))






main()