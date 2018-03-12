# Tuples are immutable ie once a value is assigned to tuple it can't be changed later

my_tuple = ("Michael", "Herman", 31, "Software Developer")
print(my_tuple[0])
# my_tuple[0] = "Umesh"   #this line cause error: TypeError: 'tuple' object does not support item assignment
print((my_tuple))


# Manipulating tuples
# Operators
# Yes, you can add two tuples:

first_tuple = (1, 2)
second_tuple = (3, 4)
third_tuple = first_tuple + second_tuple + (5, 6)
print(third_tuple)


# list() - used to convert a tuple to a list
print(list(first_tuple))
print(first_tuple)

first_list = list(first_tuple)
if 2 < 3:
    print(first_list)

