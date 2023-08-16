a = int(input())
b = int(input())

length = 0

while b >= 0:
    length += 1
    temp = b
    b = a - b
    a = temp

print(length + 1)