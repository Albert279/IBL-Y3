import inflect #import the module
p = inflect.engine() #assign p to the funcs from inflect

names = []
while True:
    try:
        name = input("enter the name ")
        names.append(name)
    except EOFError:
        print()
        break
    output = p.join(names)
    print("Adieu, adieu, to") + output