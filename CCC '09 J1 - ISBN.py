a = "9780921418"
for i in range(3):
    a += input()

total = 0
curr = 1

for num in a:
    if curr == 1:
        total += int(num)
        curr = 3
    elif curr == 3:
        total += int(num) * 3
        curr = 1
print(f'The 1-3-sum is {total}')
