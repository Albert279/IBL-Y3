# if statement
"""
x= int(input("enter the value of X "))
y= int(input("enter the value of Y "))

if x<y :
    print("X is less than Y") 
    
if x>y:
        print("X is greater than Y")
        
if x==y:
        print("X and Y are equal")
"""

marks = int(input("Enter the marks? "))  
if 95 <= marks <= 100:  
   print("Congrats ! you scored grade A ...")  
elif marks >= 90 and marks <= 95:  
   print("congratulations!!! You scored grade B + you have passed the bar")  
elif marks > 80 and marks < 90:  
   print("You scored grade B ...")  
elif (marks > 70 and marks < 80):  
   print("You scored grade C ...")  
else:  
   print("Sorry you have failed!!!")
