#List of task using f-string  - Lists have [ ]
list_of_tasks = [
    "This is the 1st task on this list",
    "This is the 2nd task on this list",
    "This is the 3rd task on this list"
]
print(list_of_tasks)
print(len(list_of_tasks))

# For loop
for task in list_of_tasks:
    print(task)

#----------------------------
print("----------------------------------")
# New example
ice_cream_flavors = [
    "vanilla",
    "Chocolate",
    "Strawberry",
    "Mint Chocolate Chip",
    "Totty Fruity"
]
print(ice_cream_flavors)
print(len(ice_cream_flavors))

for flavor in ice_cream_flavors:
    print(f"""for the ice cream flavor listed below,
          provide a captivating description that could be used 
          for promotional purpose
          Flavor:  {flavor}
          """)
    print(flavor)

print("----------------------------------")
#saving results to a new promotional list from user input
promotional_descriptions = []
for new_flavor in ice_cream_flavors:
    new_flavor = input("Please enter a new flavor:   ")
    print("this was entered for flavor",new_flavor)
    print(f"""for the ice cream flavor listed below,
          provide a captivating description that could be used 
          for promotional purpose
          Flavor:  {new_flavor}
          """)
    print("this is the new flavor user entered :",new_flavor)
    description = new_flavor
    print("this is the value in description",description)
    promotional_descriptions.append(description)
    print("this is the value in the new promotional ice cream list",promotional_descriptions)
print("this is the original ice cream list",ice_cream_flavors)