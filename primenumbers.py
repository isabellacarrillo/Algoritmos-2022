def main():
    print("Welcome to the prime calculator")
    num=int(input("Enter a number to verify if it is prime:"))
    aux=num-1
    cont=0
    if num==1:
        print("The number is not prime")
    elif num==0:
        print("The number is not prime")
    elif num<0:
        print("Invalid number")
    else:
        while aux>1:
            if num %aux==0:
             cont+=1
            aux-=1
        if cont==0:
            print("The number is prime")
        else:
            print("The number is not prime")

main()