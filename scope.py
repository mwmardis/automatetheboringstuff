spam = 42

def eggs():
    global spam
    spam = 43

print(spam)
eggs()
print(spam)

