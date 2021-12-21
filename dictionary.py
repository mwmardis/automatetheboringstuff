import sys
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])

spam = {12345: 'luggage combo', 42: 'The answer'}
print(spam)

print('size' in myCat)
print(list(myCat.keys()))

for k in myCat.values():
    print(k)
    
    
for k, v in myCat.items():
    print(k, v)
    
print('fat' in myCat.values())

print(myCat.get('size', 0))

print(myCat.get('asdf', 0))

print('I am bringing ' + str(myCat.get('asdf', 0)) + ' cats to the picnic')

myCat.setdefault('color', 'black')

print(myCat)

print(sys.argv)