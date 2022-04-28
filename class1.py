def main():
    print("Welcome!")
    weight=int(input("Please enter your weight in kilos:"))
    height=float(input("Please enter your height in meters:"))

    imc=weight/height
    print("Your body mass index is", imc)




main()