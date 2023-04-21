
# This code prompts the user to enter an email address and stores it in the variable `email`. It then
# checks if the email address is valid by using a regular expression pattern `r"^[^@]+@[^@]+\.[^@]+$"`
# which checks if the email address has the correct format. If the email address matches the pattern,
# it prints "valid", otherwise it prints "invalid". The `.strip()` method is used to remove any
# leading or trailing whitespace from the user input.
email = input("enter your emil address: ").strip()
if (r"^[^@]+@[^@]+\.[^@]+$", email):
    print ("valid")
else:
    print("invalid")
    