def main():
    word=input("Enter a word please:").lower()
    
    while not word.isalpha():
        word=input("Enter a valid word please:")
    
    if "a" in word:
        word=word.replace("a","A")
    if "e" in word:
        word=word.replace("e","E")
    if "i" in word:
        word=word.replace("i","I")
    if "o" in word:
        word=word.replace("o","O") 
    if "u" in word:
        word=word.replace("u","U")  

    print(word)
        
main()