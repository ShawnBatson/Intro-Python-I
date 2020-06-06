# print hello world
print("Hello World")
print("Hello " + "World")

# declare a variable
name = "Shawn"

# print variable
print(name)

# string concatenation
print("Hello " + name)
# `Hello ${name}`

print(f'Hello {name}')

# data structure

#Lists (not array)
p = [10, 60, 5, "Banana"]
print(p)
# add an element to the end of p
p.append(77)
print(p)

# lets loop over the list p, and print every element
for element in p:
    print(element)

# lets print the index and element at the index of p
p = [10, 60, 5, "Banana"]
for (index, element) in enumerate(p):
    print(f'element at {index} is {p[index]}')

# list comprehensions
# another way to create a list
numbers = [1, 4, 9, 16, 25]
# create a new list, of squares, from the numbers list
squares = []
for num in numbers:
    squares.append(num*num)
print(squares)

# lets use List Comprehensions
# for each element from numbers, multiply by itself, and add to cooler_squres
#[function(variable) for variable in some_list]
cooler_squares = [num*num for num in numbers]
print(cooler_squares)

# lets create a list of just even numbers
evens = [num for num in numbers if num % 2 == 0]
print(evens)

# create a new list containing only name that starts with s
names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]

# also, all names should be capitalized
s_names = [name.capitalize() for name in names if name[0].lower() == "s"]

# the verbose way of writing the above statement
s_names_verbose = []
for name in names:
    if (name[0].lower() == "s"):
        s_names_verbose.append(name.capitalize())


print(s_names)

# Dictionaries
# Otherwise known as maps/hashmaps/objects
# a key --> value datastructure
new_dict = {}

# create a dictionary with some keys and values
foods_dict = {
    'apple': "is a fruit",
    'carrot': "is a vegetable"
}
print(foods_dict)

# lets add a new key value pair
foods_dict['cucumber'] = 'is maybe a vegetable?'
print(foods_dict)

# access and print a specific element in foods dict
chosen_food = 'apple'
print(foods_dict[chosen_food])

# iterate through keys and values of a dictionary
# for element in dict, do some code

for key, value in foods_dict.items():
    print(f'{key} : {value}')

# how can we check if an element exists in a dictionary
# is apple in foods dict?
print('apple' in foods_dict)
print('banana' in foods_dict)

# TUPLES and SETS
# Tuple is a collection of a couple of elements
# Tuples

tup = (1, 2, 3, 4)
for item in tup:
    print(item)

# access a particular element
print(tup[1])

# you cannot modify tup in any way. CANNOT ALTER.

# SETS are basically dictionaries without values
# a set is UNORDERED. IF you want an ordered structure, us an array/list
# SETS ARE MUTABLE. TUPPLES ARE NOT
fruit = {'cucumber', 'apple', 'banana'}
fruit.add('pizza')

for item in fruit:
    print(item)

if 'cucumber' in fruit:
    print("I don't think cucumber is a fruit")
