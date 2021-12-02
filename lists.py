spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)

print(spam[0])

doubleSpam = [['cat', 'bat', 'rat', 'elephant'], ['cat', 'bat', 'rat', 'elephant']]

print(doubleSpam[1][1])

print(spam[-1])


print('the last item in the list is: ' + spam[-1])

print(spam[0:3])

spam[1:3] = 'dog', 'cow', 'pig'
print(spam[0:4])

del spam[2]

print(spam)

print(len(spam))

print(spam * 2)

print(list('hello'))

print('howdy' in spam)