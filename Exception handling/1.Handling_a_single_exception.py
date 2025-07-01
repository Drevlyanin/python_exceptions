try:
    # Code that may cause an error
    """
    The try keyword in Python
    is used to handle exceptions (errors).
    """
    value = int(input('Enter a number from 1 to 10: '))
except ValueError:
    """
    In example, the except block catches
    one specific exception: ValueError.
    In this case, we are informing the user
    that the data entered is not an integer data type.
    """
    print('You must enter a number from 1 to 10!')
else:
    """
    The else block contains code that is executed when
    the try block completes successfully 
    (without throwing an exception).
    """
    if (value>0) and (value<=10): # This code should not be executed if the user enters invalid data.
        print("You entered: ", value)
    else:
        print("The entered value is incorrect!") 