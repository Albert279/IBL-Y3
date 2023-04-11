import random
guess = int(input("what number do you guess: "))
number = random.randint(0, 101)
while guess != +(number):
    guess = int(input("what number do you guess: "))
    if guess == number:
        print ("Just right!!")
        break
    elif guess < number:
        print ("Too small")
    else:
        print("Too high")