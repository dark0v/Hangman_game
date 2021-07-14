import random



def hangman():
    
    word = random.choice(["pugger","littlepugger","tiger","superman","thor","pokemo","avengers","earth"])
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
            
            
            
name = input("Please, enter your name: ")
print("Welcome" , name)
print("---------------")
print("Try to guess the word in less than 10 try")

hangman()
