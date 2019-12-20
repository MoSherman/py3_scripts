# this is a script to get your 'hacker name'

import re

import name_dict

def hacker_name():
    valid_names = ['']
    print(" \nThis script can tell you your Hacker Name!")
    usr_name = input("What is your name (FirstName LastName)?: ")
    usr_name = usr_name.split()
    valid_names = [re.sub(r"[^A-Za-z]+", '', name) for name in usr_name]

    if len(usr_name) >= 2:
        name_entered = True
    else:
        name_entered = False
 
    if '' not in valid_names:
        name_valid = True
    else:
        name_valid = False

    while name_entered is False or name_valid is False:
        name_entered = False
        name_valid   = False
        usr_name = input("It looks like you used an odd character or did not enter your fullname, try again!: ")
        usr_name = usr_name.split()
        valid_names = [re.sub(r"[^A-Za-z]+", '', name) for name in usr_name]

        if len(usr_name) >= 2:
            name_entered = True

        if '' not in valid_names:
            name_valid = True

    adjective = usr_name[0][0].upper()
    animal    = usr_name[1][0].upper()
    first_name = name_dict.name_dict[adjective]['adjective']
    last_name  = name_dict.name_dict[animal]['animal']
    print("Your Hacker Name is: {0} {1}!\n".format(first_name, last_name))


hacker_name()
