def main():
    """
    The function prompts the user for their name and then calls the Hello function with the user's name
    as an argument, as well as calling the Hello function without any arguments.
    """
    name=input("what is your name? ")
    Hello(name)
    Hello()
    

def Hello(z="motherfucker"): # z creates a memory space 
    """
    The function "Hello" takes an optional argument "z" and prints a greeting message with the value of
    "z" or a default value if "z" is not provided.
    
    :param z: The parameter "z" is a string variable that has a default value of "motherfucker". If no
    argument is passed when calling the function, "z" will take the default value. If an argument is
    passed, "z" will take the value of that argument, defaults to motherfucker (optional)
    """
    print ("hello, "  , z)
    
    

main()

