import random                                                #inport random                                        

name = input("What is your name?")                           #the varible name = the computer asks what is your name
print('Good luck',name)                                      #computer prints good luck, name that you used
correct = 0                                                  #number of correct guesses = 0
rounds = 0                                                   #number of rounds = 0

while True:                                                  #while rrue
    number = random.randint(1,10)                            #computers number = random generator 1-10                  
    guesses = 5                                              #number of guesses user hasis 5
    
    while guesses > 0:                                       #while # of guesses is greater than 0
        while True:                                          #while true
            userguess= input("Guess a number between 1-10")  #user guess = computer asks ti guess computers number

            try:                                             #try
                userguess = int(userguess)                   #user guess is correct and usable
                if userguess >= 1 and userguess <= 10:       #if the guess is between 1 and 10
                    break                                    #stop code
                else:                                        #else any other # not between 1-10
                    print("enter a number between 1-10")     #print enter a #between 1-10
            except ValueError:                               #except if # is not usable again (not a valid int)
                print("Enter a number between 1-10")         #print enter a # between 1-10
        if userguess == number:                              #if the users guess is the computers number
            print("you got it")                              #print you got it
            correct += 1                                     #add one point
            break                                            #end loop
        elif userguess > number:                             #else if the guess is too high
            print("too high")                                #print too high
        else:                                                #else
            print("too low")                                 #print too low

        guesses -= 1                                         ## of guesses -1
        
    if guesses == 0:                                         #if you run out of guesses
        print("you lose")                                    #print you loose

    rounds += 1                                              #round #+1
        
    while True:                                              #while true
        playagain=input(f'{name}, you have {correct} out of {rounds}. Would you like to play again? y or n?').lower()#play again(name inputed, you have___correct out of____rounds.would you like to play again?y or n?)

        if playagain == "n":                                 #if they don't play again
            exit()                                           #stop code
        elif playagain == "y":                               #if they do play again
            break                                            #break code and play round
        else:                                                #else
            print("invalid response. y or n")                #comuter prints invalid response limit to y or n
                
            
        


        
                
            
    
        
            
            
        
