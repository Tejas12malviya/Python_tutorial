e=set() #Create empty set, sets are unindexed, duplicate values ko remove kar deta hai

d={} # Create empty dict

print(type(e))
print(type(d))



# Write a program to create a dictionary of English words with values as their Hindi translation. Provide user with an option to look it up!

a={
    "Ability":"क्षमता",
    "Agitate":"उत्तेजित करना",
    "Generous":"दयालु",
    "Admire":"प्रशंसा करना",
    "Emphasize":"बल देना"
}

print(a)

print(dict.keys(a))
print(dict.values(a))

print(a.get("Admire"))
print(a["Admire"])

print(a.get("Hello"))# Prints none
# print(a["Hello"])  , Gives error
