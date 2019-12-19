# this is a simple script to find percentages
import sys

def percentage():
    print(" \nThis script can tell you what percentage a number is of another number. (type STOP to exit)")
    whole_num = input("What number would you like to find a percent for?: ")

    if whole_num == "STOP":
        print("You have entered STOP, this python script will now exit. Goodbye!\n")
        sys.exit()

    part_num  = input("Now what number would you like to know the percent of {0}?: ".format(whole_num))

    try:
        float(whole_num)
        float(part_num)
    except ValueError:
        if part_num != "STOP":
            print("You have entered not entered a set of valid numbers for this function! Try again.")
            return percentage()
        else:
            print("You have entered STOP, this python script will now exit. Goodbye!\n")
            sys.exit()

    whole_num  = float(whole_num)
    part_num   = float(part_num)
    percent    = 100 * part_num/whole_num

    print("{0} is {1} percent of {2}".format(part_num, percent, whole_num))
    return percentage()


percentage()

