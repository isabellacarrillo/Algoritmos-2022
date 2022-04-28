def main():
    print("Welcome to the playground!")
    age=int(input("Please enter your age:"))

    if age <4:
        print("You enter for free")
    elif 4< age<18:
        print("Your ticket is 5$")
    elif age > 18:
        print("Your ticket is 10$")


main()