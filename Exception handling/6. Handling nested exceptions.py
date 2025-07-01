# Control flag for the main loop
TryAgain = True

while TryAgain:
    try:
        # Attempt to get integer input
        Value = int(input("Enter an integer: "))
    
    # Handle non-integer input
    except ValueError:
        print("You must enter an integer!")
        
        try:
            # Ask to retry
            DoOver = input("Try again (y/n)? ")
        
        # Handle unexpected input termination (e.g., Ctrl+С)
        except:
            print("Okay, see you next time!")
            TryAgain = False
        
        else:
            # Exit if user enters 'n'
            if (str.upper(DoOver) == "N"):
                TryAgain = False
    
    # Handle manual interruption (Ctrl+C)
    except KeyboardInterrupt:
        print("\nThe user has terminated the program!")
        print("See you next time!")
        TryAgain = False
    
    # Successful integer input
    else:
        print(Value)
        TryAgain = False  # Exit after success