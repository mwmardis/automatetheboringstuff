import pyperclip

bobsMom = 'say hi to bob\'s mom'

print(bobsMom)

print('Hell there!\nHow are you?\nI\'m fine')

print(r'That is carol\'s cat')

print("""Dear Alice,
      Eve's cat has been arrested for catnapping, cat burglary, and extortion. 
      Sincerely,
      Bob.""")

print(bobsMom[1:5])
print(bobsMom[-1])

spam = 'hello world'

print(spam.upper())
answer = input().upper()

if (answer == 'YES'):
    print('playing again')
    
print(answer.isupper())


print('hello world'.startswith('h'))

print(' '.join(['cats', 'rats', 'bats']))

print('hello,world'.split(','))

print('hello'.center(20, '='))

pyperclip.copy('hello!!!!!')
print(pyperclip.paste())


name = 'alice'
place = 'main street'
time = '6 pm'
food = 'turnips'

print('Hello %s, you are invited to a part at %s at %s. Please bring %s.' % (name, place, time, food))