import pprint

message = 'it was a bring cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] +1

print(count)

pprint.pprint(count)

spam = pprint.pformat(count)
print(spam)
