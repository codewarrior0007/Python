# -*- coding: cp1252 -*-
# www.practicepython.org
# Lesson # 5 - List Overlap # 1
# -------------------------------------------------------------------------------
# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements _
# that are common between the lists # If not, print a different _
# appropriate message.(without duplicates). Make sure your program _
# works on two lists of different sizes. _
# Extra: Randomly generate two lists to test this
# Extra: Write this in one line of Python (don’t worry if you can’t figure this _
# Extra: out at this point - we’ll get to it soon)
# -------------------------------------------------------------------------------

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
d = []

for number in a:
    if number in b:
        c.append(number)
        print(number, " is common in the lists")
    else:
        d.append(number)
        print(number, " is not common in the lists")

print("------------------------------------------------")
print(c," is the list of common elements")
print("------------------------------------------------")
print(d," is the list of uncommon elements")
print("------------------------------------------------")
