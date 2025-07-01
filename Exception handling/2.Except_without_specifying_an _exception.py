try:

    value = int(input('Enter a number from 1 to 10: '))
except ValueError:
    print('You must enter a number from 1 to 10!')
except:
    """
    Unlike the previous code, this code uses all error handling.
    The proposal can catch any other error.
    """
    print("Generalized error!")
else:
    if (value>0) and (value<=10):
        print("You entered: ", value)
    else:
        print("The entered value is incorrect!") 