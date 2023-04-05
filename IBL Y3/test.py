a=(8,18,28,38)#daclaring a variable a
print(type(a))#display the data type of a
print(a[1])#accessing a specific value from the tuple
print(a[1:3])#demonstrating indexing 
print(a)#display
# A Tuple is a sequence of python objects separated by commas

b=['mazda','subaru','100','mercedes',]#declaring the variable b
print(type(b))#finding out the data type of b
print(b)#display
b.remove('mazda')#removing an item from the list
print(b)
b.append('nissan')#adding an item to the list
print(b)
# A list is  a series of variables

c={"apple","cherry","banana"}#declaring variable c
print(c)#display
print(type(c))#finding the data type of c
d={"apple","banana","berries"}#declaring variable d
print('cud=',c|d)#demonstrating union in set
print(c&d)#demonstrating intersection in set
# A set is the unordered collection of items, separated by a comma and use of inside braces

e={1:'hi',2:7.5,3:'class'}#declaring variable e
print(type(e))#finding out the data type of e
print(e[2])#retrieving from the dictionary
e[3]='python'#updating the dictionary
print(e)#display
# Dictionaries are used to store a huge amount of data. They are defined with braces.

f='welcome' #declaring f
g='to python'#declaring g
print(type(f))#finding out the data type of f
print(type(g))#finding out  the datatype of g
print(f+g)#demonstrating concentration; a technique of joining 2 strings together
print(f*4)#demonstrating repetition; a technique of repeating a sequence of instruction a certain number of times
print(g[1:7])#demonstrating slicing; a technique of extracting parts of a string
print(f[-2:])#demonstrating a negative indexis supported
# A string is an ordered sequences of characters

h=True #declaring a variable h
print(h)#display
print(type(h))#finding out the data type of h
i=(-26.5)#declaring variable i
j=(10)#declaring variable j
k=i>j#declaring variable k
print(type(k))#finding out the data type of k
print(k)#display

l=5 #declaring variable
print(l)#display
print(type(l))#finding out the data type of l
m=25.5 #declaring a variable m
print(m)#display
print(type(m))#finding out the data type of m

n=range(6)#declaring a variable n
print(n)#display
print(type(n))#finding out the data type of n

o=frozenset({"Dell","Hp","Lenovo"})# declaring variable o
print(o)#display
print(type(o))#finding the data type of o

p= bytearray(5)#declaring variable p
print(p)#display
print(type(p))#finding the data type of p

string = "python"
for a in string:
    print (a)