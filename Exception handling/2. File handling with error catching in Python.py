import sys

try:
    # Try to open the file
    file = open('myfile.txt')
    
except IOError as e: # The variable e is automatically created and filled by the interpreter when entering the except block.
    # Print an error message with details
    print("Error opening file!\r\n" +
          "Error number: {0}\r\n".format(e. errno) +
          "Error text: {0}".format(e.strerror))
else:
    # If the file opened successfully
    print("File opened as expected.")
    file.close() 
