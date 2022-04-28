def main():
 phrase=input("Enter a phrase:")
 letter=input("Enter a letter:")

 n=phrase.count(letter)
 print("The number of times the letter",letter,"was repeated in the phrase is", n)
main()