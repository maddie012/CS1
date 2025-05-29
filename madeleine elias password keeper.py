#author: madeleine elias
#date: 5/7/25
#description: user enters websites, usernames, and passwords and is than able to do things to them
#challenges: aks for password at beginning, change websites, usernames, and passwords, generates random passwords, check sucurity of passwords, exports to csv file
#sources: w3schools, programiz, geeeksforgeeks
import random
import string
import csv

def check_secure(pwd):
    '''
    checks how secure a password is
    args:
        pwd: the password you want to check
    Returns:
        it will say if the password is secure or not
    Raises:
        I decided to have the other way to check passwords because it is more thorough'''
    if pwd.lower() == pwd or pwd.upper() == pwd or not any(char.isdigit() for char in pwd) or not any(char in pwd for char in list("~!@#$%^&*()_-+=")):     #checks to see if password is not secure if it has a only upper or lowercase or no special charcters or numbers
        print("password is not secure")
    else:
        print("secure")

def contains_character(characters, password):
    '''
    it checks if a element in characters is in the password
    args:
        characters: a list of certain characters that are checked if they are in
        password: a password that you want to check
    returns: it will return 1 if it is in and is used by other functiona'''
    for char in password:
        if char in characters:
            return 1
    return 0

def check_password(pwd):
    '''
    checks if a password is secure or not
    args:
        s: is the password you put in
    returns:
        how many secureity points you get'''
    security = 0

    if len(pwd) > 8:
        security += 1
    security += contains_character(list("0123456789"), pwd) + contains_character(list("~!@#$%^&*()_-+="), pwd) + contains_character(list("qwertyuiopasdfghjklzxcvbnm"),pwd) + contains_character(list("qwertyuiopasdfghjklzxcvbnm".upper()), pwd)  #for every differnt type of character it has it gets one point added to sequrity
    return security

def print_security(pwd):
    '''
    tells you if password if secure or not
    args:
        pwd: you password you want to check
    returns:
        will tell you if password is sucure or not'''
    if check_password(pwd) > 3:
        print("password is secure")
    else:
        print("password is not secure")

def add_enty(websites, usernames, passwords):
    '''
    takes current list of website usernames and passwords and add one to every list
    Args:
        Websites: list of website
        Usernames: list of usernames
        Passwords: list of passwords
    Returns:
        new list of websites usernames and passwords
    '''
    web = input("enter website ")
    user = input("enter username for website ")
    pwd = input("enter password for website (press 'g' to generate) ")

    if pwd.lower() == "g":                                             #if user presses g than it will generate a password
        pwd = generate_password()
    else:
        print_security(pwd)
    websites.append(web)
    usernames.append(user)
    passwords.append(pwd)

def print_list(websites, usernames, passwords):
    '''
    takes list of websites usernames and passwords and prints them with their respective others
    Args:
        Websites: list of website
        Usernames: list of usernames
        Passwords: list of passwords
    Returns:
        websites and their respective usernames and passwirds
    Raises:
    '''
    for i in range(len(websites)):
        print(websites[i], usernames[i], passwords[i])

def get_index(websites):
    '''
    you enter a website and it will check if it is inside the website list
    args: 
        websites: the list of website you have
    returns: 
        if the website is there it will return the index if it isn't it will say its not there'''
    while True:
        web = input('which website is it from? (enter a name of website) ')
        if web in websites:
            return websites.index(web)                        #if the website is in the lost than it will return the index of that
        else:
            print("not here")

def print_specific(website, username, password):
    '''
    takes websites, usernames and passwords and user chooses one website and can see its username and password
    Args:
        Websites: list of website
        Usernames: list of usernames
        Passwords: list of passwords
    returns:
        the website username and password of the one you choose
    Raises:
        if user dwites something that isn't in the website list and if there isn't anything in the website list yet
    '''
    i = get_index(website)
    print(f'Website: {website[i]}, Username: {username[i]}, Password: {password[i]}')

def change_entry(websites, entry_list):
    '''
    changes an entry to something else
    args:
        website: list of website
        entry_list: the list that it wants to change
    retuens the new list with the change
    raises:
        won't work if there is nothing in the list yet'''
    i = get_index(websites)
    entry_list[i] = input("Enter change: ")

def get_length():
    while True:
        try:
            length = int(input('Enter password length: '))                       #makes the input an integer
            return length
        except ValueError:
            print('Length must be an integer')

def generate_password():
    '''
    generates a new password with different characters
    args:
        length: how long you want the password to be
    returns:
        a string made up of random chacters'''
    length = get_length()
    return ''.join(random.sample(list(string.ascii_letters+'0123456789`~!@#$%^&*()-_=+'), length))     #makes a string out of random letters, characters, and letters, that is the length of length

def export_to_csv(filename, headers, *arrays):
    """
    Exports parallel arrays to a CSV file.

    Args:
        filename (str): The name of the CSV file to create.
        headers (list): A list of header names for each column.
        *arrays: Variable number of array arguments (lists or tuples).
               All arrays must have the same length.
    """
    if not arrays:
        raise ValueError("At least one array must be provided.")                            #if it isn't an array it will not work
    
    num_rows = len(arrays[0])                                                               #number or rows = how many lists there are
    for arr in arrays:                                                                      #for element in array
        if len(arr) != num_rows:
            raise ValueError("All arrays must have the same length.")                        #all arrays must have a website, username, and password
    
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)
        for i in range(num_rows):                                                            #for number of rows
            row = [arr[i] for arr in arrays]                                                 #each row has an element from an array
            csvwriter.writerow(row)                                                          #write the rows

def main():
    Websites = []                                                                              #websites, usernames, and passwords are the lists that will have the users passwords they saved
    Usernames = []
    Passwords = []

    entrance = input("hello, enter your password ")                                            #user enters password
    
    if entrance == "correct":                                                                  #if the password is corect displays welcome
        print("welcome")
    else:                                                                                      #if password is wrong leave
        print("wrong password")
        exit()

    while True:
        question = input("enter, print, specific, leave, change, generate, check, export ")    #user chooses what to do
        
        if question == "leave":                                                                #if choose leave they exit
            exit()
        elif question == "enter":                                                              #if they enter they add another website, username, password
            add_enty(Websites, Usernames, Passwords)
        elif question == "print":                                                              #if they print it displays all three lists
            print_list(Websites, Usernames, Passwords)
        elif question == "specific":                                                           #is specific displays the website, username, and password of a specific one user chooses
            print_specific(Websites, Usernames, Passwords)
        elif question == "change":                                                             #if change it allows user to change a specific website username or password 
            change = input('What would you like to change? website, username, or password: ')

            if change == "website":
                change_entry(Websites, Websites)
            elif change == "username":
                change_entry(Websites, Usernames)
            elif change == "password":
                change_entry(Websites, Passwords)
        elif question == "generate":                                                           #if generate it generates a random string that user chooses length
            print(generate_password())
        elif question == "check":                                                              #if check displays how secure it is
            yourpass = input("enter a password you want to check ")
            print_security(yourpass)
        elif question == "export":                                                             #if export, exports the lists to a csv file.
            name = input("what is name of file, write .csv at end or else it won't work ")       #user chooses what to name the file but has to end in .csv
            export_to_csv(name, ["websites", "usernames", "passwords"], Websites, Usernames, Passwords)
        else:
            print("pick something")
main()