import random

name = input("What is your name?")
print('Good luck',name)
correct = 0
rounds = 0

while True:
    number = random.randint(1,10)
    print(number)
    guesses = 5
    
    while guesses > 0:
        while True:
            userguess= input("Guess a number between 1-10")

            try:
                userguess = int(userguess)
                if userguess >= 1 and userguess <= 10:
                    break
                else:
                    print("enter a number between 1-10")
            except ValueError:
                print("Enter a number between 1-10")
        if userguess == number:
            print("you got it")
            correct += 1
            break
        elif userguess > number:
            print("too high")
        else:
            print("too low")

        guesses -= 1
        
    if guesses == 0:
        print("you lose")

    rounds += 1
        
    while True:
        playagain=input(f'{name}, you have {correct} out of {rounds}. Would you like to play again? y or n?').lower()

        if playagain == "n":
            exit()
        elif playagain == "y":
            break
        else:
            print("invalid response. y or n")
                
            
        


        
                
            
    
        
            
            
        
