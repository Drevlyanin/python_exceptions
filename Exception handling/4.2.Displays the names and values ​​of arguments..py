import sys

try:
    file = open('myfile.txt')
except IOError as e: 
    for Entry in dir(e): # Get a list of attributes associated with an error object using the dir() function.
        if not Entry.startswith("_"):
            """
            It returns a list of strings containing the attribute names that can be printed to the screen
            But only those arguments that do not begin with an underscore (_) contain useful information about the exception.
            """
            try:
                print(Entry, " = ", getattr(e, Entry))
            except AttributeError:
                print("Attribute", Entry, "not available.")
else:
    print("File opened as expected.")
    file.close()
"""
It is easy to output the attribute name, since it is contained in the variable Entry.
 But to get the value associated with this attribute, you need to use the _getattribute()
function, passing it the attribute name.
"""