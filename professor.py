import random 
while True:
    num1 = random.randint(0,4)
    num2 = random.randint(0, 4)
    sum = num1 + num2
    response = int(input(f"what is {num1} + {num2}=? "))
    ans = int(response)
    if ans != response:
        print("EEE")
    response = int(input(f"what is {num1} + {num2}=? "))

    print("Great!!" if ans == response else "wrong")
