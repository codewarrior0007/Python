# www.practicepython.org
# Lesson # 3 - List Less than Ten 
# -------------------------------------------------------------------------------
# Take a list, say for example this one:_
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]_
# and write a program that prints out all the elements of the list that are less than 5._
# Instead of printing the elements one by one, make a new list that has_
# all the elements less than 5 from this list in it and print out this new list_
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements _
# from the original list a that are smaller than that number given by the user.
# -------------------------------------------------------------------------------


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

number = int(raw_input("Choose a number: "))

number_list = []

for i in a:

	if i < number:

		number_list.append(i)

print number_list
