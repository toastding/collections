def add(*args):
    sum = 0
    for n in args:
        sum += n
        print(type(args))
    return sum


# print(add(3, 4, 15))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.color = kw.get("color")


my_car = Car(make="Nissan", model="GT-R", color="Black")
print(my_car.make)
print(my_car.model)
print(my_car.color)

