for i in range(4):
    print(i)
    
print(list(range(4)))

print(list(range(0, 100, 10)))

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
    
cat = ['fat', 'orange', 'loud']

size = cat[0]
color = cat[1]
disposition = cat[2]

size, color, disposition = cat

print(size, color, disposition)

a = 'AAA'
b = 'BBB'
a, b = b, a

spam = 42
spam = spam + 1

spam += 1