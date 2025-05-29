#password keeper
#author: madeleine elias
#date: 5/6/25
#description:
#challenges: asks for password to get in, change websites usernames and passwords,
#sources: w3schools
entrance = input("hello, enter your password ") 
if entrance == "correct":
    print("welcome")
else:
    print("wrong password")
    exit()
a = input("enter website 1 ")
d = input("enter username for website 1 ")
g = input("enter password for website 1 ")
b = input("enter website 2 ")
e = input("enter username for website 2 ")
h = input("enter password for website 2 ")
c = input("enter website 3 ")
f = input("enter username for website 3 ")
i = input("enter password for website 3 ")
Websites = [a,b,c]
Usernames = [d,e,f]
Passwords = [g,h,i]

def print_list():
    '''
    prints every element in websites, usernames and passwords
    Args: none
    Returns:
        the lists
    '''
    for i in range(len(Websites)):
        print(Websites[i], Usernames[i], Passwords[i])

def print_specific():
    whichone = input("choose website 1,2, or 3? 1/2/3 ")
    if whichone == "1":
        print(Websites[0], Usernames[0], Passwords[0])
    elif whichone == "2":
        print(Websites[1], Usernames[1], Passwords[1])
    elif whichone == "3":
        print(Websites[2], Usernames[2], Passwords[2])
    else:
        print("you didn't pick a website")

def leave():
    exit()

def change_web():
    web = input("which website do you want to change 1/2/3 ")
    change1 = input("what do you want to change it to ")
    if web == "1":
        Websites[0] = change1
    elif web == "2":
        Websites[1] = change1
    elif web == "3":
        Websites[2] = change1
    else:
        print("didn't choose a website")
    return Websites

def change_user():
    user = input("which username do you want to change 1/2/3 ")
    change2 = input("what do you want to change it to ")
    if user == "1":
        Usernames[0] = change2
    elif user == "2":
        Usernames[1] = change2
    elif user == "3":
        Usernames[2] = change2
    else:
        print("you didn't choose a username")
    return Usernames

def change_pass():
    passw = input("which password do you want to change 1/2/3 ")
    change3 = input("what do you want to change it to ")
    if passw == "1":
        Passwords[0] = change3
    elif passw == "2":
        Passwords[1] = change3
    elif passw == "3":
        Passwords[2] = change3
    else:
        print("you didn't choose a password")
    return Passwords

while True:
    question = input('''print list of websites, print specific website, leave, change websites, change usernames, change passwords? 
    print/specific/leave/change web/change user/change pass ''')
    if question == "print":
        print_list()
    elif question == "specific":
        print_specific()
    elif question == "leave":
        leave()
    elif question == "change web":
        print(change_web())
    elif question == "change user":
        print(change_user())
    elif question == "change pass":
        print(change_pass())
    else:
        print("enter which function you want")