# -*- coding: cp1252 -*-
# www.practicepython.org
# Lesson # 6 - List Comprehensions
# -------------------------------------------------------------------------------
# Let’s say I give you a list saved in a variable: _
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Write one line of Python that takes this list a and makes _
# a new list that has only the even elements of this list in it.
# -------------------------------------------------------------------------------

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [value for value in a if value%2 == 0]

print(b, "  is an example of list comprehensions")
