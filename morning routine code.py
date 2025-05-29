import time

print("ALARM")
print("It's 6:30AM")
snoozes = 0

while True:
    snooze = input("SNOOZE? YES/NO").upper()
    if snooze == "YES":
        print("SLEEP FOR 5 MIN")
        snoozes += 1
        time.sleep(2)
        if snoozes < 8:
            print("SLEEP MORE")
            time.sleep(2)
        else:
            break
    elif snooze == "NO":
        break
    else:
        print("INVALID RESPONSE")
print("GET UP")
time.sleep(1)
print("WALK TO CLOSET")
while True:
    temperature = input("OVER 60 DEGREES? YES/NO").upper()
    if temperature == "YES":
        print("WEAR SHORTS")
        break
    elif temperature == "NO":
        print("WEAR LEGGINGS")
        break
    else:
        print("INVALID RESPONSE")
print("GET CHANGED")
time.sleep(1)
print("GO TO BATHROOM")
time.sleep(1)
print("BRUSH TEETH")
print("BRUSH HAIR")
time.sleep(1)
print("GET BACKPACK")
time.sleep(1)
print("GO DOWNSTAIRS")
time.sleep(1)
while True:
    breakfast = input("LEFTOVER PANCAKES? YES/NO").upper()
    if breakfast == "YES":
        print("EAT PANCAKES")
        time.sleep(1)
        break
    elif breakfast == "NO":
        print("EAT WAFFLES")
        time.sleep(1)
        break
    else:
        print("INVALID RESPONSE")
print("PUT ON SHOES")
time.sleep(1)
while True:
    degrees = input("OVER 45 DEGREES? YES/NO").upper()
    if degrees == "NO":
        print("PUT ON COAT")
        time.sleep(1)
        print("GO TO CAR")
        time.sleep(1)
        print("GO TO SCHOOL")
        break
    elif degrees == "YES":
        print("GO TO CAR")
        time.sleep(1)
        print("GO TO SCHOOL")
        break
    else:
        print("INVALID RESPONSE")
            


