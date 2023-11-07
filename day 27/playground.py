def add(*nums):
    result = 0
    for num in nums:
        result += num
    return result
    
print(add(1,2,3,4,5,6,7,8))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n += kwargs["multiply"]
    print(n)



calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]


my_car = Car(make="Nissan", model="GT-8")
print(my_car.model)
