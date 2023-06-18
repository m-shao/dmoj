t = int(input())
ans = []


for i in range(t):
    n = int(input())
    cars = [int(input()) for i in range(n)]
    cars.reverse()

    stack = [100001]
    nextCar = 1
    valid = True
    currCar = 0
    while currCar < len(cars):
        if cars[currCar] == nextCar:
            currCar += 1
            nextCar += 1
        elif stack[-1] == nextCar:
            stack.pop()
            nextCar += 1
        elif stack[-1] < cars[currCar]:
            valid = False
            break
        else:
            stack.append(cars[currCar])
            currCar += 1

    if valid:
        ans.append("Y")
    else:
        ans.append("N")
for answer in ans:
    print(answer)