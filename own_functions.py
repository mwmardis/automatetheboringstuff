def hello(name):
    print("Hello " + name)
    
hello('Alice')
hello('Bob')

print('Hello has ' + str(len('hello')) + ' letters in it.')

def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)
print('cat', 'dog', 'mouse', sep='ABC')