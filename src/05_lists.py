# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE

y.insert(0, 1)
y.insert(1, 2)
y.insert(2, 3)
y.insert(3, 4)
print(y)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.append(9)
x.append(10)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print(x)


# Print the length of list x
# YOUR CODE HERE
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
multiple = []
for num in x:
    multiple.append(num*1000)
print(multiple)
