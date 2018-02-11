# www.practicepython.org
# Lesson # 1 - Character Input
# ------------------------------------------------------------------------
# Create a program that asks the user to enter their name and their age. _
# Print out a message addressed to them that tells them the year that they _
# will turn 100 years old.
# ------------------------------------------------------------------------
name = raw_input("Please Enter your name:    ")
age = int(raw_input("Please enter your age:      "))
year = str((2018 - age)+100)

print("Your name is " + name)
print(name + " will be 100 years old in the year  " + year)
