# www.practicepython.org
# Lesson # 2 - Odd or Even - Part 1
# -------------------------------------------------------------------------------
# Ask the user for two numbers: one number to check (call it num) and one number, _
# to divide by (check). If check divides evenly into num,tell that to the user._
# If not, print a different appropriate message.
# If the number is a multiple of 4, print out a different message.
# -------------------------------------------------------------------------------
number = int(raw_input("Please enter a number:      "))
check = int(raw_input("Please a number to divide by:      "))

if number != 0:
    if number %  4 == 0 :
        print(number, "is a multiple of 4")
    elif number %  2 == 0 :
        print(number, "is an even number")
    else:
        print(number, "is an odd number")
else:
    print(number, "is zero number")


