instructions = {}

direction = ''
magnitude = -1
pos = [0, 0]
while direction != 'q':
    direction, magnitude = input().split()
    instructions[int(magnitude)] = direction

copIns = {v: k for k, v in instructions.items()}
for ins in copIns:
    print(copIns[ins], ins)
    if copIns[ins] == 'l':
        pos[0] += ins
    elif copIns[ins] == 'r':
        pos[0] -= ins
    elif copIns[ins] == 'd':
        pos[1] += ins
    elif copIns[ins] == 'u':
        pos[1] -= ins

print(pos)
visited = []
for ins in instructions:
    if instructions[ins] == 'l':
        for i in range(ins):
            pos[0] -= i
            if pos in visited:
                print(pos[0], pos[1], 'DANGER')
                exit()
            visited.append(pos.copy())
            print(pos[0], pos[1], 'safe')
    elif instructions[ins] == 'r':
        for i in range(ins):
            pos[0] += i
            if pos in visited:
                print(pos[0], pos[1], 'DANGER')
                exit()
            visited.append(pos.copy())
            print(pos[0], pos[1], 'safe')
    elif instructions[ins] == 'u':
        for i in range(ins):
            pos[1] += i
            if pos in visited:
                print(pos[0], pos[1], 'DANGER')
                exit()
            visited.append(pos.copy())
            print(pos[0], pos[1], 'safe')
    elif instructions[ins] == 'd':
        for i in range(ins):
            pos[1] -= i
            if pos in visited:
                print(pos[0], pos[1], 'DANGER')
                exit()
            visited.append(pos.copy())
            print(pos[0], pos[1], 'safe')