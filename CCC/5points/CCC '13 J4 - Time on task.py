t = int(input())
n = int(input())
chores = [int(input()) for i in range(n)]
chores.sort()

total = 0
count = 0
for chore in chores:
    total += chore
    if total > t:
        print(count)
        break
    count += 1