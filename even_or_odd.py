# a short script using mod to determin if number is even or odd
import sys

def even_or_odd():
    print(" \nThis script can tell you if a number is even or odd. (type STOP to exit)")
    usr_num = input("What number would you like to test?: ")
 
    try:
        float(usr_num)
    except ValueError:
        if usr_num != "STOP":
            print("You have entered {0} which is a not valid number for this function!".format(usr_num))
            return even_or_odd()
        else:
            print("You have entered STOP, this python script will now exit. Goodbye!\n")
            sys.exit()

    usr_num = float(usr_num)
    print("Congrats! You have entered {0} which is a valid number for this function!".format(usr_num))

    if usr_num % 2 != 0:
        print("The number {0} is odd!".format(usr_num))
    else:
        print("The number {0} is even!".format(usr_num))

    return even_or_odd()
        

even_or_odd()

