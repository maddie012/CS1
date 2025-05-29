import random                                         #import random library
list=["Yes", "No","Maybe","Ask again later","idk"]    #list of how the magic 8 ball can answer
while True:                                           #forever loop
    question = input("Ask question")                  #tell user to ask a question
    if "?" not in question:                           #ask if ? is not in answer
        print("Not a question")                       #display not a question
    else:                                             #anything else
        print(random.choice(list))                    #picks randomly from the list
        end = input("End? Yes/No").lower()            #ask user if they want to end
        if end == "yes":                              #if they respond yes
            break                                     #stop
        else:                                         #anything else
            print("Ask again")                        #display ask again
   

  

