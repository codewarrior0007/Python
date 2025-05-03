
# Define the directory to read files from
# directory_path = "/home/ak/Downloads/python/Module3_work/L6/"
# cape_town = "cape_town.txt"
# paris = "paris.txt"
# sydney ="sydney.txt"
# tokyo = "tokyo.txt"
# istanbul = "istanbul.txt"
# rio_de_janeiro = "rio_de_janeiro.txt"


# # Print function
print("Hello World!")

# # Create a list of friends
friends_list = ["bb","cc","aa","UK"]

# #Return the number friends in the list
print(len(friends_list))


# print("----- PARAMETERS IN FUNCTION ------")
# #value of temp in F - stand alone functionality
# fahrenheit = 72
# # Calculate temp in C
# celcius = (fahrenheit - 32) * 5 / 9
# # Print the results
# print(f"{fahrenheit}degree F is equivalent to {celcius:.2f} degree C")

# # If another temp is needed you will need another temp converter
# #value of temp in F - stand alone functionality
# fahrenheit = 68
# # Calculate temp in C
# celcius = (fahrenheit - 32) * 5 / 9
# # Print the results
# print(f"{fahrenheit}degree F is equivalent to {celcius:.2f} degree C")

# functions to do repeated calculations.
def fahrenheit_to_celcius(fahrenheit):
# Calculate temp in C
    celcius = (fahrenheit - 32) * 5 / 9
# Print the results
    print(f"{fahrenheit}degree F is equivalent to {celcius:.2f} degree C")

fahrenheit_to_celcius(71)
fahrenheit_to_celcius(70)
fahrenheit_to_celcius(212)

# # function with return
print("----- READ FUNCTION WITH RETURN ------")
def fahrenheit_to_celcius(fahrenheit):
# Calculate temp in C
    celcius = (fahrenheit - 32) * 5 / 9
# Print the results
    #print(f"{fahrenheit}degree F is equivalent to {celcius:.2f} degree C")
    return(celcius)

fahrenheit = 45
celcius = fahrenheit_to_celcius(fahrenheit) 
print(celcius)
print("-----")


print("----- C to F FUNCTION  ------")
def celcius_to_fahrenheit(celcius):
# Calculate temp in C
#    celcius = (fahrenheit - 32) * 5 / 9
    fahrenheit = (celcius * 9/5) + 32
# Print the results
    print(f"{celcius}degree C is equivalent to {fahrenheit} degree F")

celcius_to_fahrenheit(0)
celcius_to_fahrenheit(100)
celcius_to_fahrenheit(13)

print("----- Meters to FT FUNCTION  ------")
def meter_to_feet(meter):
# Calculate distance in meters
    feet = (meter * 3.28084)
# Print the results
    print(f"{meter} is equivalent to {feet}")

meter_to_feet(10)
meter_to_feet(0.70)
