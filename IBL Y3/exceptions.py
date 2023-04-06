while True:
    try:
        x=int(input("enter the value of x "))
        print(f"x is {x}")
    except ValueError:
        print("x is not an intager! Try again.")
    else:
        pass
        print(f"x is {x}")