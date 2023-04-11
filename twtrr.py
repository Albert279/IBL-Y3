name = str(input("what's your name "))
vowels = ('a', 'e', 'i', 'o', 'u')
for x in name.lower():
    if x in vowels:
        name = name.replace(x, "")        
print(name)