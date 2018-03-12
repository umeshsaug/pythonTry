# Lists are mutable which means after creating a list we can modify or manipulate it

create_a_list = []
numbers_list = [1, 2, 3, 'abc']
strings_list = ["spam", "eggs", "cheese"]
mixed_list = ["Hello", [1, 2, 3], False]

print(mixed_list)
print(numbers_list)

print(numbers_list[1:2])
print(mixed_list[0:1])

lst = [1, 'a', 2.5]    
lst.insert(1,6)

lst.extend(["abc", 9])

print(lst)