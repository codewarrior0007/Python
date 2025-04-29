# Dictionary structure helps you to store key-value pairs
# Dictionary has {  }
ice_cream_flavors = {
    "Vanilla": "Classic and creamy",
    "Chocolate": "Deep and indulging",
    "Strawberry": "Sweet and fruity",
    "Mint Chocolate Chip": "Refreshing mint ice cream",
    "Cookie Dough": "Vanilla ice cream loaded with chicks of chocolate",
    "Salted Caramel": "Sweet and Salty",
    "Pistachio": "Nutty and creamy",
    "Cookie and Cream": "Vanilla ice cream packed with chunks of chocolate",
    "Mango": "Tropical and tangy",
    "Rocky Roads": "Chocolate ice cream mixed with with marshmallows"
}
print("=================================================")
print("This is the dictionary",ice_cream_flavors)
print("=================================================")
print("These are the dictionary keys",ice_cream_flavors.keys())
print("=================================================")
print("These are the dictionary values",ice_cream_flavors.values())
print("=================================================")

# Access single item in a dictionary
print("=================================================")
vanilla_description = ice_cream_flavors["Vanilla"]
print(vanilla_description)
print(ice_cream_flavors["Vanilla"])
print(ice_cream_flavors.get("Vanilla"))
print("=================================================")
chocolate_description = ice_cream_flavors["Chocolate"]
print(chocolate_description)
print(ice_cream_flavors["Chocolate"])
print(ice_cream_flavors.get("Chocolate"))
print("=================================================")

# Adding and updating elements in dictionary
print("=================================================")
print("This is the dictionary",ice_cream_flavors)
ice_cream_flavors["Oreo Cookie"] = "Vanilla with a blend of Oreo Cookie"
print("This is the dictionary with added flavor",ice_cream_flavors)
ice_cream_flavors["Oreo Cookie"] = "Vanilla with a blend of Oreo Cookie and Chocolate"
print("This is the dictionary with updated flavor",ice_cream_flavors)
print("=================================================")

# Different types of elements in dictionary
print("=================================================")
aa_facts = {
    "age":15,
    "favorite color":"blue",
    "favorite game":"pac man"
}
print("This is the aa facts dictionary",aa_facts)
print("-------------------------------------------------")

# Dictionary can store lists - useful when trying to access 
# Group related data or Storing Multiple Values for Single Key,
#  for Group Data for Processing
print("-------------------------------------------------")
print("Dictionary can store lists")
print("_________________________________________________")
aa_facts["Cat name"] = ["Orange","Smokey","Tommy"]
print("This is the update dictonary with Cat names list in it",aa_facts)
print("_________________________________________________")
aa_facts["favorite meal"] = ["Okra","Biryani","Fries"]
print("This is the update dictonary with Fav Meals list in it",aa_facts)
print("_________________________________________________")


# Task list not in order needs to be priortized 
print("=================================================")
list_of_tasks = [
    "Compose a brief email to my boss",
    "Write a birthday poem for aa",
    "Wrote 300 word  review of movie 'Accountant 2'",
    "Draft a thank-you note for my neighbor Ken",
    "Create an outline for a presentation"
]
print("This is not in order of priority list",list_of_tasks)
print("-------------------------------------------------")
# Unorganized large list, divided task by priority
high_priority_tasks = [
    "Compose a brief email to my boss",
    "Create an outline for a presentation"
]
mid_priority_tasks = [
    "Write a birthday poem for aa",
    "Draft a thank-you note for my neighbor Ken"
]
low_priority_tasks = [
    "Wrote 300 word  review of movie 'Accountant 2'"
]

print("high priorty tasks list",high_priority_tasks)
print("mid priorty tasks list",mid_priority_tasks)
print("low priority tasks list",low_priority_tasks)
print("-------------------------------------------------")

# Adding priortized tasks list to a single Dictionary
prioritized_tasks ={
   "high_priority": high_priority_tasks,
   "mid_priority": mid_priority_tasks,
   "low_priority": low_priority_tasks         
}
print("Dictionary of Prioritized Tasks",prioritized_tasks)
print("-------------------------------------------------")


# Complete high priority tasks
# Accessing 1 task based on 1 key  
for task in prioritized_tasks["high_priority"]:
    print("List of high tasks by priority",task)
    print("_________________________________________________")

# Wrong way to access task based on priority 
# Need to 1st load keys and then access task based on the priortity of the key
#for task in prioritized_tasks["high_priority","mid_priority","low_priority"]:
#    print("List of tasks by priority",task)
#    print("_________________________________________________")

# Correct way to process all the tasks based on proirity 
for priority in ["high_priority","mid_priority","low_priority"]:
    print(f"List of priority",priority)
    for tasks in prioritized_tasks[priority]:
        print(f"List of {priority} task ",tasks)
    print("_________________________________________________")


