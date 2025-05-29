import random                                                                 #cat
import os
rps = ["rock", "paper", "scissors"]                                          #cumputer's rps are rock paper or scissors
score_limit = 5 #five is the score limit

while True:                                                                   #forever loop
        gamemode = input("play number guess, rock paper scissors, or q to quit? ").lower()#choose which game to play

        if gamemode == "rock paper scissors":                                      #if they pick rock paper scissor
                p1_name = input("Player 1, enter your name: ") #player one enters name
                
                while True: #forever loop
                        play = input("One user or two? one/two").lower()#choose game mode of one player, two, always win, always lose or quit

                        if play == "one":                                                     #if you choose one player
                                p2_name = "bot" #player two is computer
                        elif play == "two":         #if you chooose two people
                                p2_name = input("Player 2, enter your name: ") #player two writes their name
                        else: #else
                            print("invalid response")#display invalid response
                            continue #go on

                        p1_score = 0#player ones score is 0
                        p2_score = 0 #player 2s score is 0

                        while p1_score < score_limit and p2_score < score_limit: #while both players score within limit
                                p1_rps = input(f"{p1_name}, enter your weapon: ").lower() #player one enters rock/paper/scissor

                                if p1_rps not in rps and p1_rps != "always win" and p1_rps != "always lose": # if player one enters not supposed to
                                        print(f"{p1_name}, please enter rock, paper, or scissors") #tell them to enter rock/paper/scissor
                                        continue#go one
                                if play == "one": #if user plays bot
                                        p2_rps = random.choice(rps) #computer chooses randomly
                                else: #else
                                        os.system("cls")#clear screen
                                        p2_rps = input(f"{p2_name}, enter your weapon: ").lower()#user two enters rock/paper/scissor
                                        os.system("cls")#clear screen

                                if p2_rps not in rps:#if player 2 doesn't pick rock/paper/scissor
                                        print(f"{p2_name}, please enter rock, paper, or scissors")#tell user two to pick rock/paper/scissor
                                        continue#go on

                                if p1_rps == "always win" and play == "one":#if user picks always win
                                        print(f"{p1_name} wins the game") #display user one wins
                                        p1_score = score_limit #user one score is limit
                                        break#break
                                if p1_rps == "always lose" and play == "one": #if user picks always lose
                                        print(f"{p1_name} loses the game")#display user one loses
                                        p2_score = score_limit#score is limit
                                        break#break
                                print(f"{p1_name} chose {p1_rps} and {p2_name} chose {p2_rps}")#if user one and two choose same thing
                                if p1_rps == p2_rps:                                             #if both rps are the same
                                        print("It's a tie")                                                  #display tie
                                        p2_score += 1#user 2 score +1
                                elif p1_rps == "scissors" and p2_rps == "rock":                       #if ply2 guess scissor and pl1 guess rock
                                        print(f"{p2_name} wins!")                                                  #display win
                                        p2_score += 1#user 2 score +1
                                elif p1_rps == "rock" and p2_rps == "paper":                       #if pl1 guess paper and pl2 says rock
                                        print(f"{p2_name} wins!")                                                  #display win
                                        p2_score += 1#user 2 score +1
                                elif p1_rps == "paper" and p2_rps == "scissors":                    #if pl1 guess scissor and pl2 guesses paper
                                        print(f"{p2_name} wins!")                                                  #display win
                                        p2_score += 1#user 2 score +1
                                else:#else
                                        print(f"{p1_name} wins!")#player one wins
                                        p1_score += 1#player 1 score +1
                                print(f"{p1_name} has {p1_score} and {p2_name} has {p2_score}")#display their scores
                        if p1_score > p2_score:#if player one score is larger
                                print(f"{p1_name} won this game!")#display player 1 won round
                        else:#else
                                print(f"{p2_name} won this game!")#display player 2 won round


            
        elif gamemode == "number guess":                                          #elif user chooses to play number guess
                number = random.randint(1, 10)#computer pick # betwen 1-10
                guesses = 0#you have 0 guesses

                while guesses < 5:#if you have less then 5 guesses
                        try:#try
                                guess = int(input("Guess a number from 1-10: "))                   #user picks number between 1-10
                        except ValueError:# if you don't pick number
                                print("Please enter a number!")#display enter number
                                continue#go on
                        if guess == number:                                                    #if the user picks the right number
                                print(f"You got it! The number was {number}")       #display you gotit                                              
                                break#break
                        elif guess > number:                                                                 #else user picks wrong number thats too big
                                print("Nope, that's not it. The number is lower.")    #diaply number is lower                                                
                        else:                                                                 #else user picks wrong number thats too small
                                print("Nope, that's not it. The number is higher.") #display number is higher                                                   
                        guesses += 1 #add one to guesses
                if guesses >= 5:#if you run out of guesses
                        print(f"You lost. The number was {number}")#display you lost

        elif gamemode == "q":                                                     #elif they decide to quit
                print("quitting")                                                 #display quitting
                break                                                             #break
        
        else:                                                                     #else
                print("invalid response")                                             #display invalid response     

            
                
