import sys

try:
    file = open('myfile.txt')
except IOError as e: 
    for Arg in e.args: 
        """
        The args property always contains a list of exception arguments in string format.
        a for loop to print each argument to the screen.
        """
        print(Arg)
else:
    print("File opened as expected.")
    file.close();

"""
However, there is one problem: the argument names are missing,
so you see the output but don't know which arguments it corresponds to.
"""