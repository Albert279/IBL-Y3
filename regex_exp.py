
import re

email = input("enter your emil address: ").strip()
if re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
    print ("valid")
else:
    print("invalid")
    