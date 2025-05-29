import time                                               #add time to code

print("ALARM")                                            #display message "Alarm"
print("It's 6:30AM")                                      #display message "It's 6:30AM"
snoozes = 0                                               # number or snoozes is 0

while True:                                               #forever loop
    snooze = input("SNOOZE? YES/NO").upper()              #ask user if they snooze yes or no make everything uppercase
    if snooze == "YES":                                   #if user says yes to snooze
        print("SLEEP FOR 5 MIN")                          #display message sleep for 5 min
        snoozes += 1                                      #add 1 more to number of snoozes
        time.sleep(2)                                     #2 sec pause                           
        if snoozes < 8:                                   #if number of snoozes less than 8        
            time.sleep(1)                                 #1 sec pause
        else:                                             #if something else
            break                                         #end loop
    elif snooze == "NO":                                  #if user replys no to snooze
        break                                             #end forever loop
    else:                                                 #if something else
        print("INVALID RESPONSE")                         #display message "Invalid response"
print("GET UP")                                           #out of loop display message "Get up"
time.sleep(1)                                             #pause for 1 sec
print("WALK TO CLOSET")                                   #display message"Walk to closet"
while True:                                               #forever loop
    temperature = input("OVER 60 DEGREES? YES/NO").upper()#ask user if its over 60 degrees make everything uppercase
    if temperature == "YES":                              #if user replies yes
        print("WEAR SHORTS")                              #display message "wear shorts"
        break                                             #end forever loop
    elif temperature == "NO":                             #if user relpies no
        print("WEAR LEGGINGS")                            #display message "wear leggings"
        break                                             #end forever loop
    else:                                                 #if something else
        print("INVALID RESPONSE")                         #display message "invalid response"
print("GET CHANGED")                                      #out of loop display message "get changed"
time.sleep(1)                                             #1 sec pause
print("GO TO BATHROOM")                                   #display message "go to bathroom"
time.sleep(1)                                             #1 sec pause
print("BRUSH TEETH")                                      #display message "brush teeth"
print("BRUSH HAIR")                                       #display message "brush hair"
time.sleep(1)                                             #1 sec pause
print("GET BACKPACK")                                     #display message "get backpack"
time.sleep(1)                                             #1 sec pause
print("GO DOWNSTAIRS")                                    #display message "go downstairs"
time.sleep(1)                                             #1 sec pause
while True:                                               #forever loop
    breakfast = input("LEFTOVER PANCAKES? YES/NO").upper()#ask user if there's leftover pancakes make everything uppercase
    if breakfast == "YES":                                #if user replies yes
        print("EAT PANCAKES")                             #display message "eat pancakes"
        time.sleep(1)                                     #1 sec pause
        break                                             #end forever loop
    elif breakfast == "NO":                               #if user replies no
        print("EAT WAFFLES")                              #display message "eat waffles"
        time.sleep(1)                                     #1 sec pause
        break                                             #end forever loop
    else:                                                 #if something else
        print("INVALID RESPONSE")                         #display message "invalid response"
print("PUT ON SHOES")                                     #out of loop display message "put on shoes"
time.sleep(1)                                             #1 sec pause
while True:                                               #forever loop                                 
    degrees = input("OVER 45 DEGREES? YES/NO").upper()    #ask user if its over 45 degrees make everything uppercase
    if degrees == "NO":                                   #if user replies no
        print("PUT ON COAT")                              #display message "put on coat
        break                                             #end forever loop
    elif degrees == "YES":                                #if user replies yes
        print("LEAVE")                                    #display message "leave"
        break                                             #end forever loop
    else:                                                 #if something else
        print("INVALID RESPONSE")                         #display message "invalid response"
if snoozes == 0:                                          #if you didn't snooze
    print("ITS 7:10")                                     #displa its 7:10
elif snoozes == 1:                                        #if you snoozed once
    print("ITS 7:15")                                     #display its 7:15
elif snoozes ==2:                                         #if you snoozed twice
    print("ITS 7:20")                                     #displat its 7:20
elif snoozes == 3:                                        #if you snoozed 3 times
    print("ITS 7:25")                                     #display its 7:25
elif snoozes == 4:                                        #if you snoozed 4 times
    print("ITS 7:30")                                     #display its 7:30
elif snoozes == 5:                                        #if you snoozed 5 times                           
    print("ITS 7:35")                                     #display its 7:35
elif snoozes == 6:                                        #if you snoozed 6 times
    print("ITS 7:40")                                     #display its 7:40
elif snoozes == 7:                                        #if you snoozed 7 times
    print("ITS 7:45")                                     #display its 7:45
else:                                                     #else
    print("ITS 7:50")                                     #display its 7:50
print("GO TO CAR")                                        #display go to ca
time.sleep(1)                                             #wait 1 sec
print("GO TO SCHOOL")                                     #display go to school
    
              
        
            


