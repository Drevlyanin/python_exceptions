# Custom exception class inheriting from ValueError
class CustomValueError(ValueError):
    # Initialize with custom error message
    def __init__(self, arg):
        self.strerror = arg  # Store error message
        self.args = {arg}    # Set exception arguments

try:
    # Raise custom exception with message
    raise CustomValueError("The value must be between 1 and 10.")
except CustomValueError as e:
    # Catch and print custom error message
    print("Exception CustomValueError!", e.strerror)