x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))

board = [[0 for i in range(8)] for i in range(8)]

def checkValid(x,y, move):
    valid = []
    if move == 1:
        if y - 2 >= 0 and x + 1 < 8:
            valid = [x + 1, y - 2]
    elif move == 2:
        if y - 1 >= 0 and x + 2 < 8:
            valid = [x + 2, y - 1]
    elif move == 3:
        if y + 1 < 8 and x + 2 < 8:
            valid = [x + 2, y + 1]
    elif move == 4:
        if y + 2 < 8 and x + 1 < 8:
            valid = [x + 1, y + 2]
    elif move == 5:
        if y + 2 < 8 and x - 1 >= 0:
            valid = [x - 1, y + 2]
    elif move == 6:
        if y + 1 < 8 and x - 2 >= 0:
            valid = [x - 2, y + 1]
    elif move == 7:
        if y - 1 >=0 and x - 2 >= 0:
            valid = [x - 2, y - 1]
    elif move == 8:
        if y - 2 >= 0 and x - 1 >= 0:
            valid = [x - 1, y - 2]
    return valid
    

def findValidSpaces(x, y):
    validSpaces = []
    for move in range(1,9):
        space = checkValid(x, y, move)
        if space:
            validSpaces.append(space)
    return validSpaces

visited = []

def bfs(board, tile):
    count = 0
    q = [[tile, 0]]
    while q:
        v = q.pop(0)
        if v[0][0] + 1 == x2 and v[0][1] + 1 == y2:
            return v[1]
        visited.append(v[0])
        for space in findValidSpaces(v[0][0], v[0][1]):
            if space not in visited:
                q.append([space, v[1] + 1])

print(bfs(board, [x1 - 1, y1 - 1]))
    