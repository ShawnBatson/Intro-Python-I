"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print(f'The value of x is %s' % x)
print(f'The value of y is %s' % y)
print(f'The value of z is %s' % z)


# Use the 'format' string method to print the same thing

one = "The value of x is {ex}".format(ex=x)
two = "The value of y is {why}".format(why=y)
three = "The value of z is {zee}".format(zee=z)

print(one + ", and " + two + ", and " + three)

# Finally, print the same thing using an f-string

print(
    f"The value of x is {x}, and The value of y is {y}, and The value of z is {z}")
