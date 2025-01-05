info={
    'Name':'Rohan',
    'Age':26,
    'Gender':'Male'
}

print(len(info))

info['Married']=True

print(info)
print(len(info))
info.pop("Gender")
print(info)

for x,y in info.items():
    # print(x)
    print(y)

# --------------------------------------------------------------------------------------------------

# Based on the dictionary:
#
# my_vehicle = {
#     "model": "Ford",
#     "make": "Explorer",
#     "year": 2018,
#     "mileage": 40000
# }
# - Create a for loop to print all keys and values
#
# - Create a new variable vehicle2, which is a copy of my_vehicle
#
# - Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4
#
# - Delete the mileage key and value from vehicle2
#
# - Print just the keys from vehicle2

my_vechicle={
    "model":"Ford",
    "make":"Explore",
    "year":2018,
    "mileage":40000
}

for x,y in my_vechicle.items():
    print(x,y)

vechicle2=my_vechicle.copy()
vechicle2['number_of_tires']=4
vechicle2.pop('mileage')
print(vechicle2)
print(my_vechicle)