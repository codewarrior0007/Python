# -*- coding: cp1252 -*-
# www.practicepython.org
# Lesson # 8 - Guessing Game 
# -------------------------------------------------------------------------------
# Generate a random number between 1 and 9 (including 1 and 9)_
# Ask the user to guess the number, then tell_
# them whether they guessed too low, too high,_
# or exactly right. (Hint: remember to use the user input _
# lessons from the very 1st exercise _
# Extras:
# Keep the game going until the user types “exit” _
# Keep track of how many guesses the user has taken, and _
# when the game ends, print this out.
# -------------------------------------------------------------------------------

import random


randnum = random.randint(1,9)
guessnum = 0
count = 0

while guessnum != randnum and guessnum != "exit":
    guessnum = raw_input("Please guess a number between 1 and 9  ")

    if guessnum == "exit":
        break

    guessnum = int(guessnum)
    count += 1

    if guessnum < randnum:
        print("you guessed too low!")
    elif guessnum >  randnum:
        print("you guessed too high!")
    else:
        print("you guessed it right!")
        print("it took only ",count, "tries to guess")
            
                         
