
"""
    The function takes user input for a greeting and returns a monetary value based on the input.
    """
def main():
    grt = str(input("what is your greeting?: "))
    answer(grt)
def answer(grt):

    if grt == "hello":
        print("$0")
    elif grt[0]== "h":
        print("$20")
    else:
        print("$100")

main()