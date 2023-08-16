n = int(input())
wood = list(map(int, input().split()))

dic1 = {}

for i in range(len(wood)):
    for j in range(i + 1, len(wood)):
        sum1 = wood[i] + wood[j]
        if sum1 in dic1:
            if i not in dic1[sum1] and j not in dic1[sum1]:
                dic1[sum1][i] = j
                dic1[sum1][j] = i
        else:
            dic1[sum1] = {i: j, j: i}
wood = []
count = 0
ll = 0
for key1 in dic1:
    if len(dic1[key1])//2 == ll:
        count += 1
    if len(dic1[key1])//2 > ll:
        count = 1
        ll = len(dic1[key1])//2
print(ll, count)
        