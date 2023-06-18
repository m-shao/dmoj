y = int(input())

def isDistinct (year):
    for digit in str(year):
        if str(year).count(digit) > 1:
            return False
    return True

while True:
    y+=1
    if isDistinct(y):
        print(y)
        break
