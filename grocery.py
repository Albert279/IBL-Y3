list = []

while True:
    items = str(input("what items would you like to purchase "))
    list.append(items)
    list1= sorted(list)
    prefix = " - " 
    choice = input("enter another item?? (yes/control-d) : ")
    if choice.casefold() == "control-d":
        break
    
for element in list1:
        print(prefix + element.upper())