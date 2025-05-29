import random                                                                 #cat
score = 0                                                                     #single player score is 0
score1 = 0                                                                    #player one score is 0
score2 = 0                                                                    #player two score is 0
score3 = 0                                                                    #always win score is 0
score4 = 0                                                                    #always lose score is 0
score5 = 0                                                                    #number guess score is 0
choices=["rock", "paper", "scissor"]                                          #cumputer's choices are rock paper or scissors
numbers=["1","2","3","4","5","6","7","8","9","10"]                            #computers number choices are 1-10
while True:                                                                   #forever loop
    gamemode = input("play number guess, rock paper scissor, or q to quit?").lower()#choose which game to play

    if gamemode == "rock paper scissor":                                      #if they pick rock paper scissor
        play = input("One user, two,always win, always lose or q to quit? one/two/always win/always lose/q").lower()#choose game mode of one player, two, always win, always lose or quit

        if play == "one":                                                     #if you choose one player
            guess = input("pick rock, paper, or scissor").lower()             #user picks rock paper or scissors
            choice = (random.choice(choices))                                 #computer makes a random choice        
            if choice == "scissor" and guess == "rock":                       #if computer guess scissor and you guess rock
                print(guess)                                                  #display your choice
                print(choice)                                                 #display computers choice
                print("Win")                                                  #display win
                score += 1                                                    #your score gets one more
            elif choice == "rock" and guess == "paper":                       #if you guess paper and computer says rock
                print(guess)                                                  #display your guess
                print(choice)                                                 #display computers choice
                print("Win")                                                  #display win
                score += 1                                                    #add one to your score
            elif choice == "paper" and guess == "scissor":                    #if you guess scissor and computer guesses paper
                print(guess)                                                  #display your choice
                print(choice)                                                 #display computers choice
                print("Win")                                                  #display win
                score += 1                                                    #add one to your score
            elif choice == guess:                                             #if both choices are the same
                print(guess)                                                  #display your choice
                print(choice)                                                 #display computers choice
                print("Tie")                                                  #display tie
            elif guess != "paper" and guess != "rock" and guess != "scissor": #if user choice isn't one of the options
                print("Invalid response")                                     #display invalid response
            else:                                                             #else
                print("Lose")                                                 #display lose
                print(guess)                                                  #display your choice
                print(choice)                                                 #display computers choice
                score -= 1                                                    #score -1
            print("Score")                                                    #display "score"
            print(score)                                                      #display users score

            #player two goes....
        elif play == "two":                                                   #else if you write two
            guess1 = input("Player One, pick rock, paper, or scissor").lower()#guess1 is player ones choice
            guess2 = input("Player Two, pick rock, paper, or scissor").lower()#guess2 is player twos choice

            #checking choices...
            if guess2 == "scissor" and guess1 == "rock":                      #if player one picks rock and player two picks scissor
                print(guess1)                                                 #display player one choice
                print(guess2)                                                 #display player two choice
                score1 += 1                                                   #player one score +1
                score2 -=1                                                    #player two score -1
                print("Player one wins")                                      #display player one wins
            elif guess2 == "rock" and guess1 == "paper":                      #elif player 2 guess rock and player 1 guess paper
                print(guess1)                                                 #display player one guess
                print(guess2)                                                 #display player two guess
                score1 += 1                                                   #player 1 score +1
                score2 -=1                                                    #player 2 score -1
                print("Player one wins")                                      #display player one wins
            elif guess2 == "paper" and guess1 == "scissor":                   #elif player two guess os paper and plauer one picks scissor
                print(guess1)                                                 #display player one guess
                print(guess2)                                                 #display user 2 guess
                score1 += 1                                                   #player 1 score +1
                score2 -=1                                                    #player 2 score -1
                print("Player one wins")                                      #display player 1 wins
            elif guess1 == "scissor" and guess2 == "rock":                    #elif player 1 pick scissor and player 2 pick rock
                print(guess1)                                                 #display player one guess
                print(guess2)                                                 #display player two guess
                score2 += 1                                                   #player two +1
                score1 -= 1                                                   #player one score -1
                print("Player two wins")                                      #display player two wins
            elif guess1 == "rock" and guess2 == "paper":                      #elif player one pick rock and player 2 pick paper
                print(guess1)                                                 #display player 1 choice
                print(guess2)                                                 #display player 2 choice
                score2 += 1                                                   #player 2 score +1
                score1 -= 1                                                   #player 1 score -1
                print("Player two wins")                                      #display player two wins
            elif guess1 == "paper" and guess2 == "scissor":                   #elif player 1 picks paper ans player 2 picks scissors
                print(guess1)                                                 #display player 1 choice
                print(guess2)                                                 #displayer player 2 choice
                score2 += 1                                                   #player 2 score +1
                score1 -= 1                                                   #player 1 score -1
                print("Player two wins")                                      #display player two wins
            elif guess1 == guess2:                                            #elif both guesses are the same
                print(guess1)                                                 #display player 1 choice
                print(guess2)                                                 #display player 2 choice
                print("tie")                                                  #display tie
            else:                                                             #else
                print("Invalid response")                                     #display invalid response
            print("player one score:")                                        #display player 1 score
            print(score1)                                                     #display score
            print("player two score:")                                        #display player2 score
            print(score2)                                                     #display player 2 score    
            
        elif play == "always win":                                            #elif user picks always win
            guess3 = input("player pick rock, paper, or scissor").lower()     #user picks rock paper or scissor
            if guess3 == "scissor":                                           #if they pick scissor
                print(guess3)                                                 #display guess
                print("paper")                                                #display paper
                print("win")                                                  #display win
                score3 += 1                                                   #score +1
            elif guess3 == "rock":                                            #elif user picks rock
                print(guess3)                                                 #display user choice
                print("scissor")                                              #display scissor
                print("win")                                                  #display win
                score3 += 1                                                   #score +1
            elif guess3 == "paper":                                           #elif user picks paper
                print(guess3)                                                 #display user choice
                print("rock")                                                 #display rock
                print("win")                                                  #display win
                score3 += 1                                                   #score +1
            else:                                                             #else
                print("Invalid response")                                     #display invalid response
            print("Cheater score:")                                           #display cheater score
            print(score3)                                                     #display user score
        
        elif play == "always lose":                                           #elif user chooses to always lose
            guess4 = input("player pick rock, paper, or scissor").lower()     #user picks rock paper or scissors
            if guess4 == "scissor":                                           #if user guesses scissor
                print(guess4)                                                 #display user guess
                print("rock")                                                 #display rock
                print("lose")                                                 #display lose
                score4 -= 1                                                   #score - 1
            elif guess4 == "rock":                                            #elif user picks rock
                print(guess4)                                                 #display guess
                print("paper")                                                #display paper
                print("lose")                                                 #display lose
                score4 -= 1                                                   #score - 1                          
            elif guess4 == "paper":                                           #elif guess paper
                print(guess4)                                                 #display guess
                print("scissor")                                              #display scissor
                print("lose")                                                 #display lose
                score4 -= 1                                                   #score - 1
            else:                                                             #else
                print("Invalid response")                                     #display invalid response
            print("Loser score:")                                             #display loser score
            print(score4)                                                     #display score
            
        elif play == "q":                                                     #elif user choice to quit
            print("quitting")                                                 #display quitting
            break                                                             #break
        else:                                                                 #else
            print("Invalid response")                                         #display invalid response          
            
        if score > 10 or score < -10:                                         #if score is greater than ten or less than -10
            print("single player score is reseting")                          #display single user score if reseting
            score = 0                                                         #single user score is 0
        elif score1 > 10 or score1 < -10 or score2 > 10 or score2 < -10:      #elif player one or two scores are above 10 or lower than -10
            print("multi-player scores are reseting")                         #display multiplayer scores are reseting
            score1 = 0                                                        #player 1 score is 0
            score2 = 0                                                        #player 2 score is 0
        elif score3 > 10 or score3 < -10:                                     #elif always win score is above 10 or below -10
            print("cheater scores are reseting")                              #display cheater scores are reseting
            score3 = 0                                                        #always win score is 0
        elif score4 > 10 or score4 <-10:                                      #elif always lose score is above 10 or below -10
            print("Loser scores are reseting")                                #display loser scores are reseting
            score4 = 0                                                        #always lose score is 0
        else:                                                                 #else
            print(" ")                                                        #display
                      
        reset = input("reset all scores? yes/no").lower()                     #ask if user wants to reset all scores
        if reset == "yes":                                                    #if they say yes
            score = 0                                                         #single user score is 0
            score1 = 0                                                        #player 1 score is 0
            score2 = 0                                                        #player 2 score is 0
            score3 = 0                                                        #always win score is 0
            score4 = 0                                                        #always lose score is 0
        elif reset == "no":                                                   #elif user says no
            print(" ")                                                        #display
        else:                                                                 #else
            print("Invalid response")                                         #display invalid response

            
    elif gamemode == "number guess":                                          #elif user chooses to play number guess
        pick = input("pick whole number from 1-10").lower()                   #user picks number between 1-10
        number = (random.choice(numbers))                                     #computer randomly chooses number
        if pick == number:                                                    #if the user picks the right number
            print(pick)                                                       #display user guess
            print(number)                                                     #display computers guess
            print("win")                                                      #display win
            score5 += 1                                                       #score + 1
        else:                                                                 #else user picks wrong number
            print(pick)                                                       #print what user guessed
            print(number)                                                     #display the number
            print("lose")                                                     #display lose
            score5 -= 1                                                       #score - 1
        print("number guess score:")                                          #display number guess score
        print(score5)                                                         #display score
        resetnumber = input("reset number guess score? yes/no").lower()       #ask user to reset
        if resetnumber == "yes":                                              #if user say yes
            print("number guess scores are reseting")                         #display score is reseting
            score5 = 0                                                        #score is 0
        elif resetnumber == "no":                                             #elif user says no
            print("continue")                                                 #display continue
        else:                                                                 #else
            print("invalid response")                                         #display invalid response
        if score5 > 10 or score5 < -10:                                       #if score is greater than ten or less than -10
            print("number guess score is reseting")                           #print number guess scores are reseting
            score5 = 0                                                        #score is 0
        else:                                                                 #else
            print(" ")                                                        #display nothing
            
    elif gamemode == "q":                                                     #elif they decide to quit
            print("quitting")                                                 #display quitting
            break                                                             #break
        
    else:                                                                     #else
        print("invalid response")                                             #display invalid response
        

            
                
