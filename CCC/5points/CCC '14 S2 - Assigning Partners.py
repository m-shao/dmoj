yes = int(input())
g1 = input().split()
g2 = input().split()
dict1 = {}

def boo():
    for a, b in zip(g1, g2):
        if a == b:
            return False
        dict1[a] = b
        if b in dict1:
            if dict1[b] != a:
                return False
    return True

if boo():
    print("good")
else:
    print("bad")
    