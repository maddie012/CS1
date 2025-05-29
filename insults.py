import random     

insults = ["You three-inch fool", "You froward and unable worm", "Thou lily-liver'd boy", "Thou wit's as thick as a Tewkesbury mustard", "I am sick when I do look on thee", "I'll beat thee, but I would infect my hands", "Methink'st thou art a general offence and every man should beat thee", "More of you conversation would infect my brain", "Peace, ye fat guts", "The rankest compound of villainous smell that ever offended nostril", "The tartness of your face sours ripe grapes", "There's no more faith in thee than in a stewed prune", "Thine face is not worth sunburning", "Thou art a boil, a plague sore", "Thou art as fat as butter", "Here is the babe, as loathsome as a toad", "Like the toad; ugly and venomous", "Thou art unfit for any place but hell", "Thou cream faced loon", "Thou damned and luxurious mountain goat", "Thou elvish-mark'd, abortive, rooting hog", "Thou leathern-jerkin, crystal-button, know-pated, agatering, puke-stocking, caddis-garter, smooth-tounue, Spanish pouch", "Thou lump of foul deformity", "That poisonous bunch-back'd toad", "Thou sodden-witted lord! Thou hast no more brain than I have in mine elbows","Thy tongue outvenoms all the worms of Nile", "Would thou wert clean enough to spit upon", "Would thou wouldst burst", "You are as a candle, the better burnt out", "You scullion! You rampallian! You fustilarian! I'll tickle your catastrophe!", "Your brain is as dry as the remainder biscuit after voyage", "Villain, I have done thy mother", "Heaven truly knows that thou art false as hell", "Out of my sight! Thou dost infect mine eyes"] #list of insults
#list of shakespear insults

while True:#forever loop
    stop = input("quit? y/n: ") #ask user to quit
    
    if stop == "y": #if user says yes
        break #break
    else:
        try:
            items = int(input("How many insults do you need? ")) #ask user how many item
        except ValueError: #except if it isn't an integer
            print("enter a number") #tell user to enter number
            continue                 #start from beginning
        
        for i in range(items):             #for how many insults user wants
            index = random.randint(0,33)          #index in random number 0-33
            print(insults[index])               #show the random insult
