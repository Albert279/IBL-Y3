# This code takes input from the user for their name, and then converts the name to a format where
# each uppercase letter is preceded by an underscore and converted to lowercase. The resulting string
# is then printed, starting from the second character (to remove the initial space added to the `res`
# variable).
name = input("What is your name: ")
ans = " "
for i in name:
    if(i.isupper()):
        ans+= "_" + i.lower()
    else:
        ans+= i
print(ans[1:])