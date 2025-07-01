try:
    value = int(input('Enter a number from 1 to 10: '))
    """
    We can handle multiple errors in one except clause.
    But only if exceptions are handled according to the same logic.
    """
except (ValueError, KeyboardInterrupt):
    print('You must enter a number from 1 to 10!')
    
else:
    if (value>0) and (value<=10):
        print("You entered: ", value)
    else:
        print("The entered value is incorrect!") 