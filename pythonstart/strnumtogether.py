# Mixing strings with computations or date: f-strings

# Equivalent degrees  F to C
print("==================")
print("F to C",((75 - 32) * 5 / 9))
print("==================")



print(" Parenthesis then Multiple then divide then add then sub")
a = 75 - 32
print("a is 75 - 32   :",a)

b = a * 5 
print("b is a * 5    :",b)

c = b / 9
print("c is b / 9    :",c)

print(f"The temperature 75F in C is {(75 - 32) * 5 / 9}C")


# Dog year calculation 
print("aa is 15 years old")
print(f"aa in {15/7} dog years old ")


print("bb is 19 years old")
print(f"bb in {19/7} dog years old ")

print("cc is 44 years old")
print(f"aa in {44/7} dog years old ")


print("zz is 52 years old")
print(f"aa in {52/7} dog years old ")


#How data is displayed in f-strings - No digit accer decimal restriction 
print("YX is 28 years old")
print(f"aa in {28/7} dog years old ")

# :.0f = show nothing accer decimal
print("YX is 28 years old")
print(f"aa in {28/7:.0f} dog years old ")

# :.1f = show 1 vaule accer decimal
print("YX is 28 years old")
print(f"aa in {28/7:.1f} dog years old ")

# :.2f = show 1 vaule accer decimal
print("YX is 28 years old")
print(f"aa in {28/7:.2f} dog years old ")



# Multiline f-strings - measurement conversion
print(f""" 
    Most countries use the metric system.
      
    So you need to convert recipe units to your local measuring system
      
    For example, 8 fluid ounces of milk is {8 * 29.5735} mi.
    And 100ml of water is {100 / 29.5735} fluid ounces  
""")


#-- To work on later 
# Cat year calculation
# print("aa is 15 years old")
# #1 cat_year = 15 human years
# #2 cat years = 15 + 9 = 24 human years
# #3 cat year = 24 + 4
# #4 cat years = 28 + 4
# #5 cat year = 32 + 4
# #6 cat years = 40 years
# #7 cat years = 40 + 4
# #8 cat years = 48 years
# #9 cat years = 52 years 
# print(f"aa in {15/15} cat years old ")

# print("bb is 19 years old")
# print(f"bb in {24/19} cat years old ")

# print("cc is 44 years old")
# print(f"cc in {44/44} cat years old ")

# print("zz is 52 years old")
# print(f"aa in {52/7} dog years old ")


