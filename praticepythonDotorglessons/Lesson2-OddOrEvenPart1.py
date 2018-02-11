# www.practicepython.org
# Lesson # 2 - Odd or Even - Part 1
# ------------------------------------------------------------------------
# Csk the user for a number. Depending on whether the number is even or odd, _
# print out an appropriate message to the user. _
# ------------------------------------------------------------------------
number = int(raw_input("Please enter a number:      "))
mod = number % 2

if mod > 0:
    print("The number you picked is an odd number.")
else:
    print("The number you picked is an even number.")
