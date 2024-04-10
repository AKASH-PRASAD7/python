# String

# '' or "" can be used to define a string

msg = 'Hello World'
print(msg)

print(msg[0:5]) # Hello
print(msg[6:]) # World
print(msg[:5]) # Hello
print(msg[-1]) # d
print(msg[0:9:2]) # HloWr
print(msg[::-1]) # dlroW olleH


# String methods

print(msg.upper()) # HELLO WORLD
print(msg.lower()) # hello world
print(msg.capitalize()) # Hello world
print(msg.title()) # Hello World
print(msg.swapcase()) # hELLO wORLD
print(msg.startswith('H')) # True
print(msg.endswith('d')) # True
print(msg.strip()) # Hello World
print(msg.replace('World','Universe')) # Hello Universe
print(msg.find('World')) # 6
print(msg.count('l')) # 3
print("hello" in msg) # False

# String formatting

fruit='apple, banana, cherry, date'

print(fruit.split()) # ['apple,', 'banana,', 'cherry,', 'date']
print(fruit.split(',')) # ['apple', ' banana', ' cherry', ' date']
print(fruit.split(',',2)) # ['apple', ' banana', ' cherry, date']

name='John'
age=25

msg1='My name is {} and I am {} years old'
print(msg1.format(name,age)) # My name is John and I am 25 years old

colors=['red','green','blue']
print("".join(colors)) # redgreenblue
print(" ".join(colors)) # red green blue
print(", ".join(colors)) # red, green, blue
print(" and ".join(colors)) # red and green and blue

path="C:\\Users\\John\\Documents\\Python\\Basics"
print(path) # C:\Users\John\Documents\Python\Basics
print(r"C:\Users\John\Documents\Python\Basics") # C:\Users\John\Documents\Python\Basics
