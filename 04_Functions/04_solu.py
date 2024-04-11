import math

def area_circum(radius):
    circumference=2*math.pi*radius
    area=math.pi*(radius**2)
    return area,circumference

a,c= area_circum(5)


def greet(name="Akash"):
    print("hello",name)

greet()


def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num*factorial(num-1)

print(factorial(4))


cube = lambda x:x**3

print(cube(9))


def sum_all (*args):
   return sum(args)

print(sum_all(1,2,3,4))



def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy = "Dr. Jackaal")


def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i



for num in even_generator(10):
    print(num)