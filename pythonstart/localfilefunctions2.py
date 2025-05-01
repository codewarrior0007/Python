from IPython.display import Markdown, display, HTML
import pandas as pd 
import io
import os
from globl_functions import * # loads all the the whole functions
#from helper_functions import celsius_to_fahrenheit, fahrenheit_to_celcius, meter_to_feet, get_llm_response
from math import *
from statistics import *
from random import *


# Define the directory to read files from
directory_path = "file path"
globl_functions = "globl_functions.py"
file1 = "file1.txt"
file2 ="file2.txt"
file3 = "file3.txt"
file4 = "file4.txt"
file5 = "file5.txt"

celsius_to_fahrenheit(20)

fahrenheit_to_celcius(78)

meter_to_feet(5)

# renspose = get_llm_response("What is the capital of France?")
# print(renspose)

# Math
print(pi)
print(type(pi))
floor(5.7)
print(type(floor))

#statistics
my_friends_heights = [160, 172, 155, 165]
print(mean(my_friends_heights))
print(stdev(my_friends_heights))

#random
spices = ["cumin", "turmeric", "oregano", "paprika"]
vegetables = ["lettuce", "tomato", "carrot", "broccoli"]
proteins = ["chicken", "tofu", "beef", "fish", "tempeh"]

random_spices = sample(spices,3)
random_vegetables = sample(vegetables,2)
random_proteins = sample(proteins,3)

print(random_spices)
print(random_vegetables)
print(random_proteins)
