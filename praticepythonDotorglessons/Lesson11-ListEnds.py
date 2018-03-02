# -*- coding: cp1252 -*-
# www.practicepython.org
# Lesson # 11 - List Ends
# -------------------------------------------------------------------------------
# Write a program that takes a list of numbers  _
# (for example, a = [5, 10, 15, 20, 25]) _
# and makes a new list of only the first and last elements  _
# of the given list. For practice, write this code inside a function.
# -------------------------------------------------------------------------------

a_list = [5, 10, 15, 20, 25]

def list_ends(a_list):
    
    z = [a_list[0], a_list[len(a_list)-1]]
    return z

z = list_ends(a_list)
print(z) 
