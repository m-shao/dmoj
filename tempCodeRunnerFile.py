n = int(input())
rounds = [list(map(int, input().split())) for i in range(n)]

a = 100
b = 100

print(rounds)

for round in rounds:
    if round[1] > round[0]:
        a -= round[1]
    elif round[0] > round[1]:
        b -= round[0]
        
print(a)
print(b)