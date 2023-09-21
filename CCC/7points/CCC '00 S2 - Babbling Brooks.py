n = int(input())
rivers = [int(input()) for i in range(n)]
ins = 0
instructions = []
while (True):
    ins = int(input())
    if ins == 77:
        break
    index = int(input()) - 1
    if ins == 99:
        left = rivers[index]*(int(input())/100)
        rivers.insert(index + 1, rivers[index] - left)
        rivers[index] = left
    elif ins == 88:
        rivers[index] += rivers[index + 1]
        rivers.pop(index + 1)

for river in rivers:
    print(round(river), end=" ")

