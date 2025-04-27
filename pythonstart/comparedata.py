# food_preferences_aa = {
#     #"dietary_restructions": "vegitarian",
#     "favirotite_ingredients":["mushroom","olives"],
#     "experience_level":["intermediate"],
#     "maximum_spice_level":6
# }

# print("aa food preferences:",food_preferences_aa)

# # Add element to mbbe sure aa gets veggie food
# food_preferences_aa["is_vegitarian"] = True

# print("aa food preferences:",food_preferences_aa)


# New scenario
aa_age = 15  # 
cc_age = 10  # 
aa_age = 19  # 
dd_age = 17  # 
bb_age = 15  # 

print("aa is older than cc    :",aa_age > cc_age)
print("cc is older than aa    :",aa_age < cc_age)
print("aa is older than dd    :",aa_age > dd_age)
print("dd is older than aa    :",aa_age < dd_age)

is_aa_older_than_cc = aa_age > cc_age
print("is aa older than cc    :",is_aa_older_than_cc)

is_cc_older_than_aa = aa_age < cc_age
print("is cc older than aa    :",is_cc_older_than_aa)

are_aa_samw_age_as_bb = aa_age <= bb_age
print("is aa older than bb    :",are_aa_samw_age_as_bb)

print(aa_age == cc_age)
print(aa_age == aa_age)
print(aa_age == dd_age)
print(aa_age == bb_age)

print("aa" == "cc")

are_aa_cc = True
are_aa_aa = False
are_aa_dd = True
are_aa_bb = True

print(are_aa_cc and are_aa_aa)
print(are_aa_cc or are_aa_aa)
print(are_aa_aa or are_aa_cc)
print(are_aa_dd and are_aa_dd)




