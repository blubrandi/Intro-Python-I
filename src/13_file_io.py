"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

dir = "/Users/brandi/Documents/Code_Stuff/Computer Science/Week 1 - Intro to Python and OOP/Day 1 - Intro To Python I/Project/Intro-Python-I/src/"
file_name1 = "foo.txt"

file = open(dir + file_name1, "r")
print(file.read())
file.close()
print(file.closed)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

file_name2 = "bar.txt"

file2 = open(dir + file_name2, "r+")
file2.write("something here \nand something else \none last time")
print(file2.read())
file2.close()
print(file2.closed)

# Todo: // File is created and written to, but doesn't print in terminal