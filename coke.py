remaining_cost = 50
while remaining_cost > 0:
    print("remaining cost is ", remaining_cost)
    coin = int(input("Insert coin "))
    remaining_cost -= coin
    
if coin in ["25", "10", "5"]:
    remaining_cost -= coin
change =abs(coin)
print("change is ", change)