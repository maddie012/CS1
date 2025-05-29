#Authors: Madeleine Elias
#Date: 4/4/25
#Description: the menu asks you how many items you want then gives you random items with sides and adds up the prices at the end. The insults asks you how many you want then creates shakespearean insults from three different words.
#Challenges: the sides have a price that is added to the total, you are able to stop, if you don't put an integer for the answer the program won't crash, the shakespear insults
#Sources: W3schools

import random    #import random

mains = ["cauliflower", "tilapia fillet", "pork loin", "salmon", "potatoes", "three color squash", "eggplant", "steak", "baguette"] #list of main dishes
prices = [20, 25, 28, 30, 18, 20, 22, 30, 20]  #list of the prices
flairs = ["with balsamico", "with garlic and olive oil", "with minted yougurt", "with chutney", "salad", "with salsa", "over sticky rice", "au jus", "with basmati rice"] #list of sides
flairprices = [3, 5, 6, 3, 5, 6, 8, 5, 10] #list of side prices
ainsult = ["artless", "bawdy", "beslubbering", "bootless", "churlish", "cockered", "clouted", "craven", "currish","dankish", "dissembling", "droning", "errant", "fawning", "fobbing", "froward", "frothy", "gleeking", "goatish", "gorbellied", "impertinent", "infectious", "jarring", "loggerheaded", "lumpish", "mammering", "mangled", "mewling", "paunchy", "pribbling", "puking", " puny", "qualling", "rank", "reeky", "roguish", "ruttish", "saucy", " spleeny", "spongy", "surly", "tottering", "unmezzled", "vain", "venomed", "villainous", "warped", "wayward", "weedy", "yeasty"]
binsult = ["base-court", "bat-fowling", "beef-witted", "beetle-headed", "boil-brained", "clapper-clawed", "clay-brained", "common-kissing", "crook-pated", "dismal-dreaming", "dizzy-eyed", "doghearted", "dread-bolted", "earth-vexing", "elf-skinned", "fat-kidneyed", "fen-sucked", "flap-mouthed", "fly-bitten", "folly-fallen", "fool-born", "full-gorged", "guts-gripping", "half-faced", "hasty-witted", "hadge-born", "hell-hated", "idle-headed", "ill-breeding", "ill-nutured", "knotty-pated", "milk livered", "motley-minded", "onion-eyed", "plume-plucked", "pottle-deep", "pox-marked", "reeling-ripe", "rough-hewn", "rude-growing", "rump-fed", "shard-borne", "sheep-biting", "spur-galled", "swag-bellied", "tardy-gaited", "tickle-brained", "toad-spotted", "unchin-snouted", "weather-bitten"]
cinsult = ["apple-john", "baggage", "barnacle", "bladder", "boar-pig", "bugbear", "bum-bailey", "canker-blossom", "clack-dish", "clotpole", "coxcomb", "codpiece", "death-token", "dewberry", "flap-dragon", "flax-wench", "flirt-gill", "foot-licker", "fustilarian", "giglet", "gudgeon", "haggard", "harpy", "hedge-pig", "horn-beast", "hugger-mugger", "joithead", "lewdster", "lout", "maggot-pie", "malt-worm", "mammet", "measle", "minnow", "miscreant", "moldwarp", "mumble-news", "nut-hook", "pigeon-egg", "pignut", "puttock", "pumpion", "ratsbane", "scut", "skainsmate", "strumpet", "varlot", "vassal", "whey-face", "wagtail"]
    
while True: #forever loop

    stop = input("quit? y/n: ") #ask user to quit
    
    if stop == "y": #if user says yes
        break #break
    
    else: #else
        question = input("menu or insults: ").lower()#asks user if they want menu or insults generator
        if question == "menu":#if they want the menu
            total = 0       #total price is 0
        
            try:
                items = int(input("How many menu items do you need? ")) #ask user how many item
            except ValueError: #except if it isn't an integer
                print("enter a number") #tell user to enter number
                continue                 #start from beginning
                
            for i in range(items):                                  #repet for how many items the user asked for
                sideindex = random.randint(0,8)                        #the computer picks number between 0-8
                index = random.randint(0,8)                         #computer picks another number between 0-8
                print(f'{mains[index]} ${prices[index]}, {flairs[sideindex]} ${flairprices[sideindex]}')    #display the main flair and price the computer randomly choose.
                total += prices[index]                                #add the price of the food to the total price
                total += flairprices[sideindex]                            #add the price of the side to the total cost
            print(total)
        #display the total price
            
        elif question == "insults":  #if they want insults generator
            try:
                amount = int(input("How many insults do you need?"))#asks how many insults they want
            except ValueError:#except if it isn't an integer
                print("enter a number")#tell user to enter number
                continue#start from beginning

            for i in range(amount):           #repeat for how many insults the user asked for
                number = random.randint(0,49)            #picks random number 0-49
                number2 = random.randint(0,49)                #random number 0-49
                number3 = random.randint(0,49)                          #random number 0-49
                print(f'{ainsult[number]}, {binsult[number2]}, {cinsult[number3]}') #displays the insults they randomly choose
        else:                          #if they don't say insults or menu
            print("decide menu or insults")  #tells user to pick menu or insults

        
             
             

    
