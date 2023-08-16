instructions = []

street = ""
direction = ""

dirdic = {
    "L": "RIGHT",
    "R": "LEFT"
}

while street != "SCHOOL":
    direction = input()
    street = input()
    instructions.append([direction, street])

instructions = instructions[::-1]

for ind, ins in enumerate(instructions):
    if ins[1] != "SCHOOL":
        print(f"{ins[1]} street.")
    if ind + 1 == len(instructions):
        print(f"Turn {dirdic[ins[0]]} into your HOME.")
    else:
        print(f"Turn {dirdic[ins[0]]} onto", end=" ")

    
        