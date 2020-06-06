"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading

f = open('src/foo.txt', 'r')

# Print all the contents of the file, then close the file

print(f.read())

f.close()

print(f.closed)
# Note: pay close attention to your current directory when trying to open "foo.txt"


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

bar = open("src/bar.txt", "w+")


bar.write("This is line 1 of arbitrary text \n" "This is line 2 of arbitrary text \n" "This is line 3 of arbitrary text \n" "adding a fourth line just because")

bar = open("bar.txt", "r")

print(bar.read())
