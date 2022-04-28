def main():
    number=int(input("Enter a number to calculate its factorial:"))
    num1=1

    if number==0:
        print("The factorial is ",number)
    elif number==1:
        print("The factorial is ", number)
    else:
        for i in range(1,number+1):
            num1=num1*i
        print("The factorial is", num1)
            



main()