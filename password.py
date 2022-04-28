def main(): 
    print("Welcome")
    password1="melwood"
    username=input("Enter yur user name:")
    password=input("Enter your password:")

    if password==password1:
        print("The password is correct")
    else:
        while password!=password1:
            password=input("Enter the correct password:")
            print("The password is correct!")

main()