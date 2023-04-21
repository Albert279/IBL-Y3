"""
    The function takes user input for a greeting and returns a value based on whether the greeting
    starts with "hello", "h", or something else.
    """

def main():
    
    greeting = input("Please enter your greeting: ")
    print("The value is:", value(greeting))


def value(greeting):
    if greeting.lower().startswith("hello"):
        return 0
    elif greeting.lower().startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()