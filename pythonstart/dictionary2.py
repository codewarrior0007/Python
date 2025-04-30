# Dictionaries are useful way to organize variables 
# associated with a single entity, like a friend.

food_preferences_aa = {
    "dietary_restrictions":"vegitarian",
    "favorite_ingrediants":["Okra","rice","curry","fries","noodles"],
    "experience_level":"intermediate",
    "maximum_spice_level":"4"
}
print("Dictionary",food_preferences_aa)
print("---")
print("Dictionary Keys",food_preferences_aa.keys())
print("---")
print("Dictionary Values",food_preferences_aa.values())
print("---")

# Using all the values in the dictionary to create a custom recipe
recipe = f"""Please suggest a recipe that tries to include
the following ingrediants:
{food_preferences_aa['favorite_ingrediants']}.
The recipe should adhere to the following dietary restrictions:
{food_preferences_aa['dietary_restrictions']}.
The difficulty of the recipe should be:
{food_preferences_aa['experience_level']}.
The maximum spice level on the scale of 10 should be:
{food_preferences_aa['maximum_spice_level']}.
"""
print("The recipe is:   ",recipe)

print("-------------------------------------------------")



