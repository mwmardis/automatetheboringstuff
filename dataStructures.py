import pprint

cat = {'name': 'watson', 'color': 'orange', }

allCats = []
allCats.append({'name': 'whiskey', 'color': 'gray'})
allCats.append(cat)

pprint.pprint(allCats)


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

pprint.pprint(theBoard)

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    
printBoard(theBoard)

print(type(42))

pprint.pprint(type(42))