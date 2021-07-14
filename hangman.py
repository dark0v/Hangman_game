import random



def hangman():
    
    word = random.choice(["pugger","littlepugger","tiger","superman","thor","pokemon","avengers","earth"])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''
    
    while len(word) > 0:
        main = ""
        missed = 0
        
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + ""
        if main == word:
            print(main)
            print("You win!")
            break
        
        print("Guess the word:" , main)
        guess = input()
                 
        
        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()
            
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("You have 9 turns left")
                print("  --------------  ")
            if turns == 8:
                print("You have 8 turns left")
                print("  --------------  ")
                print("         0        ")
            if turns == 7:
                print("You have 7 turns left")
                print("  --------------  ")
                print("         0        ")                
                print("         |        ")
            if turns == 6:
                print("You have 6 turns left")
                print("  --------------  ")
                print("         0        ")                
                print("         |        ")                
                print("        /         ")
            if turns == 5:
                print("You have 5 turns left")
                print("  --------------  ")
                print("         0        ")                
                print("         |        ")                
                print("        / \       ")
            if turns == 4:
                print("You have 4 turns left")
                print("  --------------  ")
                print("       \ 0        ")                
                print("         |        ")                
                print("        / \       ")              
            if turns == 3:
                print("You have 3 turns left")
                print("  --------------  ")
                print("       \ 0 /      ")                
                print("         |        ")                
                print("        / \       ")    
            if turns == 2:
                print("You have 2 turns left")
                print("  --------------  ")
                print("       \ 0 /|     ")                
                print("         |        ")                
                print("        / \       ")    
            if turns == 1:
                print("You have 1 turns left")
                print("Be careful. Breaths are numbered.")
                print("  --------------  ")
                print("       \ 0_|/     ")                
                print("         |        ")                
                print("        / \       ")    
            if turns == 0:
                print("You loose")
                print("Sad day. A kind man has died.")
                print("  --------------  ")
                print("         0_|      ")                
                print("        /|\       ")                
                print("        / \       ")
                break                  
                
name = input("Please, enter your name: ")
print("Welcome" , name)
print("---------------")
print("Try to guess the word in less than 10 try")

hangman()
