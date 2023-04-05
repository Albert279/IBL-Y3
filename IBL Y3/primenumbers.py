for j in range(2,51):
    for i in range(2,j):
        if j%i==0:
            print(j,'is not a prime number')
            break
    else:
        print(j,'is a prime number')