# -*- coding: cp1252 -*-
# www.practicepython.org
# Lesson # 9 - List of Overlapping Comprehensions
# -------------------------------------------------------------------------------
# Take two lists, say for example these two: _
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements  _
# that are common between the lists (without duplicates). Make sure your _
# program works on two lists of different sizes. Write this using at _
# least one list comprehension
# -------------------------------------------------------------------------------

import random

a = random.sample(range(1,30), 12)

b = random.sample(range(1,30), 16)

result = [i for i in set(a) if i in b]

print(result)
