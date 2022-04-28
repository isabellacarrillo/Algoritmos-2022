def main():
    print("Welcome to the Pizzería Bella Napoli")
    print("1. Vegetarian Pizza")
    print("2. Regular Pizza")
    choice=int(input("Enter what pizza you want:"))

    if choice==1:
        print("1. Pepper")
        print("2. Tofu")
        condiment=int(input("Enter the topping you want:"))
        if condiment==1:
            print("Vegetarian Pizza with mozzarella, tomato and pepper")
        elif condiment==2:
            print("Vegetarian Pizza with mozzarella, tomato and tofu")

    elif choice==2:
        print("1. Pepperoni")
        print("2. Ham")
        print("3. Salmon")
        topping=int(input("Enter the topping you want:"))
        if topping==1:
            print("Regular Pizza with mozzarella, tomato and pepperoni")
        elif topping==2:
            print("Regular Pizza with mozzarella, tomato and ham")
        elif topping==3:
            print("Regular Pizza with mozzarella, tomato and salmon")








main()