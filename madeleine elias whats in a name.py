 #author: Madeleine Elias
#date: 9/3/25
#description: asks for name or word and tests it with functions
#sources: old codes, w3school


import random
def count_vowels(name):
    '''
    counts the vowels in the name
    Args:
        name: the name that the user inputed 
    returns:
        the number of vowels in the name'''
    count = 0
    for i in name:
        if i == "a" or i == "e" or i =="i" or i == "o" or i == "u"or i=="y":
            count = count + 1
        else:
            count = count + 0
    return count

def reverse_display(name):
    '''
    reverses the name and prints it
    Args:
        name: the name the user inputed
    returns:
        the name backwards'''
    return name[::-1]

def palindrome(name1):
    '''
    check if the name is a palindrome and prints true or false depending on if it is
    Args:
        name1: the first name of the user after the  full name got put into the function first_name()
    returns:
        true or false depending on the answer'''
    revname = name1[::-1]
    print(name1 == revname)

def count_consonant(name):
    '''counts the number of consonants 
    Args:
        name: the name the user inputed
    returns:
        the number of consonants divided by the number of total charicters in the word'''
    total = 0
    for i in name:
        total = total + 1
    count = 0
    for i in name:
        if i == "q" or i =="w" or i =="r" or i=="t" or i=="p"or i=="s"or i=="d"or i=="f"or i=="g"or i=="h"or i=="j"or i=="k"or i=="l"or i=="z" or i=="x" or i=="c" or i=="v" or i=="b" or i=="n" or i=="m":
            count = count +1
        else:
            count = count + 0
    frequency = count/total
    return frequency

def first_name(name):
    '''
    finds the first name/word in what user inputed by stoping where the space is
    Args:
        name: the name the user inputed
    returns:
        the first name'''
    firname = ""
    for i in name:
        if i == " ":
            break
        else:
            firname += i
    return firname

def last_name(name):
    '''
    finds the last name by going backwards to find where the space is a turning it the right way again
    Args:
        name: the name the user inputed
    returns:
        The last name'''
    last = name[::-1]
    lstnm = ""
    for i in last:
        if i == " ":
            break
        else:
            lstnm += i
    rightnm = lstnm[::-1]
    return rightnm

def middle_name(name):
    '''
    finds the middle names by counting the idex until getting to the first space and then counts backwards until getting to the last space to get the index and then the middle name is what is between them. numfor is the count going forward and numback is the count going back
    Args:
        name: the name the user inputed
    returns:
        the middle names'''
    numfor = 0
    numback = len(name)
    for i in name:
        if i == " ":
            break
        else:
            numfor = numfor + 1
    numfor = numfor + 1
    for i in name[::-1]:
        if i == " ":
            break
        else:
            numback = numback - 1
    nim = (name[numfor:numback])
    return nim
    
def hyphen(name3):
    '''
    finds out if there is a hyphen in the last name using the function last_name
    Args:
        name3: last name of the user fron function last_name()
    returns:
        true or false depending if there is a hyphen in the last name'''
    random = 0
    for i in name3:
        if i == "-":
            return True
        else:
            random = random +0
    return False
            

def random_name():
    '''
    function chooses a random length between 5-15 for the length of the name. then it joins random letters for that length to get a random name
    Args:
        name: the name the user inputed
     returns:
        a random string of letters for the random name '''
    length = random.randint(5,15)
    return''.join(random.sample(list('qwertyuiopasdfghjklzxcvbnm'),length))

def initials(name1,name2,name3):
    '''
    function finds initials by first using the outputs of functions first_name, middle_name, last_name then converting them to list and printing the first letter of each using index
    Args:
        name1: the first name of the user after it got put into the function first_name()
        name2: the middle name of the user after it got put into the function middle_name()
        name3: the last name of the user after it got put into the function last_name()
    returns:
        initials of user input'''
    first = list(name1)
    middle = list(name2)
    last = list(name3)
    all = (first[0],middle[0],last[0])
    return all

def lower(name):
    '''
    function converts the letters to the octal value which is a letter to see if it is uppercase. If it is it adds 32 to convert it to its lowercase counterpart.
    Args:
        name: the name the user inputed
    returns:
        the name but will all characters as lowercase'''
    namout = ""
    for letter in name:
        if ord(letter)>64 and ord(letter)<91:
            num = ord(letter)
            num = num+32
            letter = chr(num)
            namout = namout+letter
        else:
            namout = namout+letter
    return namout

def upper(name):
    '''
    function converts letters to octel value and tests if they are lowercase. if they are it subtracts 32 to convert it to uppercase equivelant.
    Args:
        name: the name the user inputed
    returns:
        the name but with all characters as uppercase'''
    namout = ""
    for letter in name:
        if ord(letter)>96 and ord(letter)<123:
            num = ord(letter)
            num = num-32
            letter = chr(num)
            namout = namout+letter
        else:
            namout = namout+letter
    return namout

def main():
    name = input("enter your fullname ")
    name1 = first_name(name)
    name2 = middle_name(name)
    name3 = last_name(name)

    print("number of vowels:")
    print(count_vowels(name))

    print("reverse:")
    print(reverse_display(name))

    print("frequency of consonants:")
    print(count_consonant(name))

    print("random name:")
    print(random_name())

    print("first name:")
    print(first_name(name))

    print("middle name:")
    print(middle_name(name))

    print("last name:")
    print(last_name(name))

    print("uppercase:")
    print(upper(name))

    print("lowercase:")
    print(lower(name))

    print("initials:")
    print(initials(name1,name2,name3))

    print("is it a palindrome")
    palindrome(name1)

    print("does it contain hyphen")
    print(hyphen(name3))

main()


'''
Total functions:
    count_vowels
    reverse_display
    palindrome
    count_consonant
    first_name
    last_name
    middle_name
    hyphen
    random_name
    initials
    lower
    upper
'''