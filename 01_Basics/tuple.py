# Tuple

# Tuple is a collection of items which is ordered and unchangeable. Allows duplicate members.

colors = ('red', 'green', 'blue')

print(colors) # ('red', 'green', 'blue')
print(colors[0]) # red
print(colors[-1]) # blue
print(colors[1:]) # ('green', 'blue')
print(colors[:2]) # ('red', 'green')
print('red' in colors) # True
print('yellow' in colors) # False
print(len(colors)) # 3
print(colors.count('red')) # 1
# print(colors[1]='yellow') # TypeError: 'tuple' object does not support item assignment