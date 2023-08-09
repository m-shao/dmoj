#4/5
floor = int(input())
r = int(input())
c = int(input())
house = [list(input()) for i in range(r)]
tileCount = 0
roomCount = 0

def checkBoundries(direction, tile):
    x, y = tile
    res = True
    if direction == "up":
        if y - 1 < 0:
            res = False
    if direction == "down":
        if y + 1 >= r:
            res = False
    if direction == "right":
        if x + 1 >= c:
            res = False
    if direction == "left":
        if x - 1 < 0:
            res = False
    return res
    

def bfs(tile):
    ct = 0
    q = []
    
    house[tile[1]][tile[0]] = "I"
    q.append(tile)
    
    while q:
        # print(q)
        next1 = q.pop(0)
        ct += 1
        if checkBoundries("up", next1):
            if house[next1[1] - 1][next1[0]] != "I":
                house[next1[1] - 1][next1[0]] = "I"
                q.append([next1[0], next1[1] - 1])
        if checkBoundries("down", next1):
            if house[next1[1] + 1][next1[0]] != "I":
                house[next1[1] + 1][next1[0]] = "I"
                q.append([next1[0], next1[1] + 1])
        if checkBoundries("right", next1):
            if house[next1[1]][next1[0] + 1] != "I":
                house[next1[1]][next1[0] + 1] = "I"
                q.append([next1[0] + 1, next1[1]])
        if checkBoundries("left", next1):
            if house[next1[1]][next1[0] - 1] != "I":
                house[next1[1]][next1[0] - 1] = "I"
                q.append([next1[0] - 1, next1[1]])
    return ct

rooms = []

for col, room in enumerate(house):
    for row, tile in enumerate(room):
        if tile == ".":
            
            rooms.append(bfs([row, col]))
rooms.sort(reverse=True)


for room in rooms:
    if tileCount + room > floor:
        break
    else:
        tileCount += room
        roomCount += 1
print(f'{roomCount} rooms, {floor - tileCount} square metre(s) left over')


