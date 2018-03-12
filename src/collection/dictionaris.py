# Dictionary is mutable it can be modified after creation

my_dict = {1:"Umesh", 2:"Sanjay", 3:"Modi", 4:"Green", 5: "Blue", 2:"Red"}

print(my_dict)



# Dictionary methods
print(my_dict[3])   # Modi

print(my_dict.items())


print(my_dict.get(5))       # Blue

my_dict.update({3:"Yello"})

print(my_dict)