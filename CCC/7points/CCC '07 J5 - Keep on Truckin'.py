#12/21

motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]

a = int(input())
b = int(input())
c = int(input())
motels = motels + [int(input()) for i in range(c)]
motels.sort()

length = 13 + c

routes = []
def findRoutes(distance):
    if distance >= length:
        routes.append(0)
        return
    maxDistance = motels[distance] + b
    minDistance = motels[distance] + a
    possible = []
    motel = distance + 1
    while motels[motel] < minDistance:
        motel += 1
        if motel > length:
            motel-=1
            break
    while motels[motel] <= maxDistance:
        possible.append(motel)
        motel += 1
        if motel > length:
            break

    for possibility in possible:
        findRoutes(possibility)

findRoutes(0)
print(len(routes))