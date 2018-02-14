# -*- coding: cp1252 -*-
# -------------------------------------------------------------------------------
# www.practicepython.org
# Lesson # 4 - Divisors
# -------------------------------------------------------------------------------
# Create a program that asks the user for a number and then prints out _
# a list of all the divisors of that number. (If you don’t know what _
# a divisor is, it is a number that divides evenly into another number _
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
# -------------------------------------------------------------------------------


number = int(raw_input("Choose a number: "))

number_list = list(range(1,number+1))

divisor_list = []

for i in number_list:

	if number % i == 0:

		divisor_list.append(i)

print (divisor_list)
