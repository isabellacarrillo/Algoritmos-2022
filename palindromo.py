def main():
    word=input("Enter a word:")
    word1=word[::1]
    print(word1)

    if word==word1:
        print("Esta palabra es un palindromo")
    else:
        print("Esta palabra no es un palindromo")

main()