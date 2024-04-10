# Dictonaries

# Dictonaries are unordered collections of items. 
# While other compound data types have only value as an element, a dictonary has a key-value pair.

super_hero = {
    'name': 'Batman',
    'real_name': 'Bruce Wayne',
    'city': 'Gotham'
}

print(super_hero) # {'name': 'Batman', 'real_name': 'Bruce Wayne', 'city': 'Gotham'}
print(super_hero['name']) # Batman
print(super_hero.get('city')) # Gotham
print(super_hero.get('power')) # None
print(super_hero.get('power', 'No power')) # No power
print(super_hero.keys()) # dict_keys(['name', 'real_name', 'city'])
print(super_hero.values()) # dict_values(['Batman', 'Bruce Wayne', 'Gotham'])

super_hero['city'] = 'Metropolis'
print(super_hero) # {'name': 'Batman', 'real_name': 'Bruce Wayne', 'city': 'Metropolis'}
print(super_hero.pop('city')) # Metropolis
print(super_hero.popitem()) # ('real_name', 'Bruce Wayne'
del super_hero['name'] # {'name': 'Batman'}
super_hero.clear() # {}
new_super_hero = super_hero.copy() # {'name': 'Batman', 'real_name': 'Bruce Wayne', 'city': 'Gotham'}
new_super_hero = dict(super_hero) # {'name': 'Batman', 'real_name': 'Bruce Wayne', 'city': 'Gotham'}
new_super_hero = dict.fromkeys(super_hero) # {'name': None, 'real_name': None, 'city': None}



for key in super_hero:
    print(key, super_hero[key]) # name Batman, real_name Bruce Wayne, city Metropolis

for key, value in super_hero.items():
    print(key, value) # name Batman, real_name Bruce Wayne, city Metropolis

if 'city' in super_hero:
    print('city is in super_hero') # city is in super_hero

print(len(super_hero)) # 3

# Nested Dictonaries

super_hero = {
    'name': 'Batman',
    'real_name': 'Bruce Wayne',
    'city': 'Gotham',
    'powers': {
        'intelligence': 100,
        'strength': 80
    }
}

print(super_hero['powers']['intelligence']) # 100

# Comprehension
    
squares = {i: i**2 for i in range(10)} # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

super_hero = {key: value for key, value in super_hero.items() if key != 'city'} 
print(super_hero) # {'name': 'Batman', 'real_name': 'Bruce Wayne'}


# Methods

# clear() - Removes all items from the dictonary
# copy() - Returns a shallow copy of the dictonary
# fromkeys() - Returns a dictonary with the specified keys and values
# get() - Returns the value of the specified key
# items() - Returns a list containing a tuple for each key value pair
# keys() - Returns a list containing the dictonary's keys
# pop() - Removes the element with the specified key
# popitem() - Removes the last inserted key-value pair
# setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update() - Updates the dictonary with the specified key-value pairs
# values() - Returns a list of all the values in the dictonary



