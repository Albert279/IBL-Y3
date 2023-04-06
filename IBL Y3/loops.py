number_of_times = 0
while number_of_times < 3:
    print("Hello world")
number_of_times += 1

    
    
#for loop using the range method
for hello_world in range(0, 5):
    print("hello_world" )

#loop using the asteric method
print("hello world\n" * 5)

#for loop usning the underscore and range method
for _ in range(4):
    print("hello world1")

while True:
    x = int(input("Enter the value of x "))
    if 0 < x < 5:
        print("hello_world\n" * x)
        break
    else:
        continue
    
#function and loops
def main():
    number = get_number()
    hello_world(number)
def get_number():
    while True:
        x = int(input("Enter the vakue of x "))
        if x > 0:
            break
    return 

def hello_world(n):
    for _ in range(n):
        print("Hello world")
    return   
main()