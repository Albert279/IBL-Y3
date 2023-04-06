cars=['mazda','subaru','kia','mercedes',]
print(cars[0])
for car in cars:
    if car == "subaru":
        break
print(car)

cars.append('nissan')
print(cars)

cars.remove('mazda')
print(cars)
    
