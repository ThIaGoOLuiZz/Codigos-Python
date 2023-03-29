print("Welcome to Hangman Game!!\n")

correctWord = input("What's the secret word?: ")
print("--------------------------------------------")
print("\n")
print("You have 5 attemps to find the secret word!")
print("\n")

correctWord = correctWord.upper()

# FUNCTION TO SET LEN OF SET()

def lenSet(correctWord):
    letrasLista = set()
    for lista in correctWord:
        if isinstance(lista, str):
            letrasLista.add(lista)
    letrasLista = len(letrasLista)
    
    return letrasLista

letterList = lenSet(correctWord)

# FUNCTION TO VALIDATE THE LETTER

def validator(word, letrasLista):

    correctLetter = set()
    
    life = 5
    
    while life > 0:  
        
        letter = input("Letra: ")
        letter = letter.upper()
            
        print("")
        
        if letter in word:
            
            for x in word:
                if x == letter:
                    correctLetter.add(x)
            
                else:
                    continue
       
            for y in word:
                if y in correctLetter:
                   print(y, end=" ")
                else:
                   print('_', end=" ")
        
        else:
            life = life - 1
            print("Oh no! You lose a life!")
            print(f"Now, you have {life} attemps to find the secret word!!\n\n")
            
        number = len(correctLetter)
            
        if letrasLista == number:
            print("\n\nCongrats, you find the word!!")
            break
          
        if life == 0:
            print("You lose the game, better luck next time!")
            break
        print("\n")          
        
    
        
    return

validator(correctWord, letterList)