try:
    value = int(input('Enter a number from 1 to 10: '))
    
"""
When handling multiple exceptions, it is generally
recommended to catch each exception with its own except clause.
This allows you to customize the handling for each exception
and gives the user insight into what exactly went wrong.
"""

except ValueError:
    print('You must enter a number from 1 to 10!')
except KeyboardInterrupt:
    print("You stopped the program manually.")
    
else:
    if (value>0) and (value<=10):
        print("You entered: ", value)
    else:
        print("The entered value is incorrect!") 