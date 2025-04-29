#Task completion on their time to complete 
task_list = [
    {
        "description":"Compose a brief email to my boss ...",
        "time_to_complete":  3
    },
    {
        "description":"Create an outline for a presentation ...",
        "time_to_complete": 60
    },
    {
        "description":"Write a 300 word review  ...",
        "time_to_complete": 30
    },
    {   
        "description":"Create a shopping list  ...",
        "time_to_complete": 5
    }
]

task = task_list[0]
print(task)

print("-------------------------------------------------")

# if statement
task = task_list[0]
print(task)
if task["time_to_complete"] <= 5:
   task_to_do = task["description"]
   print(task_to_do) 
print("_________________________________________________")
task = task_list[1]
print(task)
if task["time_to_complete"] <= 5:
   task_to_do = task["description"]
   print(task_to_do) 
print("_________________________________________________")
task = task_list[2]
print(task)
if task["time_to_complete"] <= 5:
   task_to_do = task["description"]
   print(task_to_do) 
print("_________________________________________________")
task = task_list[3]
print(task)
if task["time_to_complete"] <= 5:
   task_to_do = task["description"]
   print(task_to_do) 
print("_________________________________________________")


print("-------------------------------------------------")

# For loop with if
for task in task_list:
   if task["time_to_complete"] <= 5:
      task_to_do = task["description"]
      print(task_to_do)
      print("___________________________________________")

# For loop with if-else
for task in task_list:
   if task["time_to_complete"] <= 5:
      task_to_do = task["description"]
      print(task_to_do)
      print("___________________________________________")
   else:
      print(f"To complete later: {task['time_to_complete']} time to complete.")
      print("___________________________________________")

print("-------------------------------------------------")


# For loop with if-else - Append to new list to compelte later
tasks_for_later = []
for  task in task_list:
   if task["time_to_complete"] <= 5:
      task_to_do = task["description"]
      print(task_to_do)
      print("___________________________________________")
   else:
      tasks_for_later.append(task)
      print(f"To complete later: {task['time_to_complete']} time to complete. Saving for later.")
      print("___________________________________________")

print(tasks_for_later)
print("___________________________________________")


print("-------------EXTRA EXERCISE-------------------------")

ice_cream_flavors = [
    "Vanilla", "Strawberry","Mint Chocolate Chip",
    "Cookies and Cream","Rocky Road","Butter Pecan",
    "Pistashio","Salted Caramel","Chocolate","Mango"
]
for flavor in ice_cream_flavors:
   if flavor == 'Chocolate':
      print(f"The list of flavors contains {flavor}, Andrew's fav.")

print("-------------------------------------------------")


# For loop with if-else - Append to new list to compelte later
tasks_for_later = []
for  task in task_list:
   if task["time_to_complete"] <= 5:
      task_to_do = task["description"]
      print(task_to_do)
      print("___________________________________________")
   else:
      tasks_for_later.append(task)
      print(f"To complete later: {task['time_to_complete']} time to complete.Task Description: {task['description']}. Saving for later.")
      print("___________________________________________")

print(tasks_for_later)
print("___________________________________________")
