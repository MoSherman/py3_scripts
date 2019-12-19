# a short script using mod to determin if number is even or odd

def even_or_odd():
    print(" \nThis script can tell you if a number is even or odd.")
    usr_num = input("What number would you like to test?: ")
 
    try:
        float(usr_num)
    except ValueError:
        print("You have entered {0} which is a not valid number for this function!".format(usr_num))
        return even_or_odd()

    usr_num = float(usr_num)
    print("Congrats! You have entered {0} which is a valid number for this function!".format(usr_num))

    if usr_num % 2 != 0:
        print("The number {0} is odd!".format(usr_num))
    else:
        print("The number {0} is even!".format(usr_num))

    return even_or_odd()
        

even_or_odd()

