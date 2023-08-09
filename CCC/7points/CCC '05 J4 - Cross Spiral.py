#does not work
outX = int(input())
outY = int(input())
inX = int(input())
inY = int(input())
steps = int(input())

x = outX - inX*2 - 1
y = 0
direction = 0
room = []
stepCounter = 0

for i in range(inY):
    room.append([1 for i in range(inX)] + [0 for i in range(x + 1)] + [1 for i in range(inX)])
for i in range(outY - inY*2):
    room.append([0 for i in range(outX)])
for i in range(inY):
    room.append([1 for i in range(inX)] + [0 for i in range(x + 1)] + [1 for i in range(inX)])
    
def canMove(direction, currTile):
    # print(direction, currTile)
    x, y = currTile
    res = []
    if direction == 0:
        if x + 1 < outX:
            if not room[y][x + 1]:
                res = [x + 1, y]
        else:
            res = []
    elif direction == 1:
        if y + 1 < outY:
            if not room[y + 1][x]:
                res = [x, y + 1]
    elif direction == 2:
        if x - 1 > -1:
            if not room[y][x - 1]:
                res = [x - 1, y]
    elif direction == 3:
        if y - 1 > -1:
            if not room[y - 1][x]:
                res = [x, y - 1]
    return res

def nextDir(direction, currTile):
    res = -1
    if direction == 0:
        if canMove(0, currTile):
            res = 0
        else:
            res = 1
    elif direction == 1:
        if canMove(0, currTile):
            res = 0
        elif canMove(1, currTile):
            res= 1
        elif canMove(2, currTile):
            res = 2
    elif direction == 2:
        if canMove(1, currTile):
            res = 1
        elif canMove(2, currTile):
            res= 2
        else:
            res = 3
    elif direction == 3:
        if canMove(2, currTile):
            res = 2
        elif canMove(3, currTile):
            res= 3
        elif canMove(0, currTile):
            res = 0
    return res

while True:
    direction = nextDir(direction, [x,y])
    if direction != -1:
        x,y = canMove(direction, [x,y])
        room[y][x] = 1
        stepCounter += 1
        if steps == stepCounter:
            print(x + 1)
            print(y + 1)
            break
    else:
        print(x + 1)
        print(y + 1)
        break
for row in room: 
    print(row)
    
    

