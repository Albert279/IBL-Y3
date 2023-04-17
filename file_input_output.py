name = input("what is your name? ")


file = open("names.txt", "a")#append(add data in the file without) 
file.write(f"{name}\n")
file.close()




with open("name.txt", "a") as file:
    file.write(f"{name}\n")



with open("name.txt","r") as file:
    for line in file:
        print("Hello, ", line.strip())