try:
    #Create custom ValueError instance
    Ex = ValueError()  
    #Add custom error message
    Ex.strerror = "The value must be between 1 and 10."  
    #Trigger the exception manually
    raise Ex  
except ValueError as e:
    #Catch and display custom error
    print("Exception ValueError!", e.strerror)  