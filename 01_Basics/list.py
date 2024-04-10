teas=['black tea', 'oolong tea', 'white tea', 'green tea', 'herbal tea']


print(teas[0]) # black tea
print(teas[1]) # oolong tea
print(teas[1:3]) # ['oolong tea', 'white tea']
print(teas[1:4:2]) # ['oolong tea', 'green tea']
print(teas[-1]) # herbal tea
teas[1:2] = 'jasmine tea'

print(teas) # ['black tea', 'j', 'a', 's', 'm', 'i', 'n', 'e', ' ', 't', 'e', 'a', 'white tea', 'green tea', 'herbal tea']

teas[1:2] = ['jasmine tea']

print(teas) # ['black tea', 'jasmine tea', 'white tea', 'green tea', 'herbal tea']

teas[1:2] = ['jasmine tea', 'chamomile tea'] # ['black tea', 'jasmine tea', 'chamomile tea', 'white tea', 'green tea', 'herbal tea']

teas[1:2]=[] # ['black tea', 'chamomile tea', 'white tea', 'green tea', 'herbal tea']


for tea in teas:
    print(tea) # black tea, chamomile tea, white tea, green tea, herbal tea

for tea in teas:
    print(tea, end='-')  # black tea-chamomile tea-white tea-green tea-herbal tea-

for i in range(len(teas)):
    print(teas[i]) # black tea, chamomile tea, white tea, green tea, herbal tea

if "coffee" in teas:
    print('coffee is in teas') # nothing

teas.append('coffee') # ['black tea', 'chamomile tea', 'white tea', 'green tea', 'herbal tea', 'coffee']

teas.insert(1, 'milk tea') # ['black tea', 'milk tea', 'chamomile tea', 'white tea', 'green tea', 'herbal tea', 'coffee']

teas.remove('milk tea') # ['black tea', 'chamomile tea', 'white tea', 'green tea', 'herbal tea', 'coffee']

teas.pop() # ['black tea', 'chamomile tea', 'white tea', 'green tea', 'herbal tea']

# Comprehension

square = [i**2 for i in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

teas = [tea for tea in teas if tea != 'black tea'] # ['chamomile tea', 'white tea', 'green tea', 'herbal tea']




