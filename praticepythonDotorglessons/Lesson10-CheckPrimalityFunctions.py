# -*- coding: cp1252 -*-
# www.practicepython.org
# Lesson # 10 - Check Primality Functions
# -------------------------------------------------------------------------------
# Ask the user for a number and determine whether the number is prime or not.: _
# For those who have forgotten, a prime number is a number that has no divisors._
# You can (and should!) use your answer to Exercise 4 to help you.
# -------------------------------------------------------------------------------

number = int(raw_input('Insert a number: '))

a = [x for x in range(2, number) if number % x == 0]


def is_it_prime(n):
	if number > 1:
		if len(a) == 0:
			print('This number is prime')
		else:
			print('This number is NOT prime')
	else:
		print('This number is NOT prime')	

is_it_prime(number)
