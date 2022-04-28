def main():
    num=input("Enter a number to verify its sum:")
    suma(num)

    print("The sum is: ",suma(num))

def suma(num):

    if int(num)<10:
        return num
    sum=0
    for digit in str(num):
        sum+=int(digit)
    return sum
    


main()