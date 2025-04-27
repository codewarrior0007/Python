# How we create a list in Python 
# Lists are a data type in Python that can hold multiple pieces of data.
# This reduces the need for repetitive variable assigments.
# Lists have [ ]
# List with strings
friend_list = ["HH","II","KK","LL"] 
print(friend_list)
print(type(friend_list))
print(len(friend_list))

# Accessing individual values in a list
friend_list1 = friend_list[0]  # First value in the list
print(friend_list1)

friend_list2 = friend_list[1]  # 2nd value in the list
print(friend_list2)

friend_list3 = friend_list[2]  # 3rd value in the list
print(friend_list3)

friend_list4 = friend_list[1]  # 4th value in the list
print(friend_list4)


#Adding new element to the list
print(friend_list)
friend_list.append("JJ")
print(friend_list)
print(len(friend_list))
friend_list.append("CC")
print(friend_list)
print(len(friend_list))


#Removing elements from the list
friend_list.remove("LL")
print(friend_list)
print(len(friend_list))
friend_list.remove("II")
print(friend_list)
print(len(friend_list))

#List with numbers
list_ages = [42,28,30]
print(list_ages)
print(len(list_ages))
## Add
list_ages.append(99)
print(list_ages)
print(len(list_ages))
## Remove
list_ages.remove(28)
print(list_ages)
print(len(list_ages))



#List of task using f-string
list_of_tasks = [
    "This is the first task on this list",
    "This is the 2nd task on this list",
    "This is the 3rd task on this list"
]
print(list_of_tasks)
print(len(list_of_tasks))

## Add
list_of_tasks.append("This is the 4th on this list")
print(list_of_tasks)
print(len(list_of_tasks))

## Remove
list_of_tasks.remove("This is the 2nd task on this list")
print(list_of_tasks)
print(len(list_of_tasks))
