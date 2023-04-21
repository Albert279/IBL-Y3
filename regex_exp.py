
# This code is checking if the input email address is valid or not using regular expressions. The `re`
# module is imported to use regular expressions. The user is prompted to enter an email address, which
# is then stripped of any leading or trailing whitespace. The regular expression
# `r"^[^@]+@[^@]+\.[^@]+$"` is used to match the email address pattern. If the email address matches
# the pattern, the code prints "valid", otherwise it prints "invalid".
import re

email = input("enter your emil address: ").strip()
if re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
    print ("valid")
else:
    print("invalid")
    