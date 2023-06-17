a = input()
letters = "IOSHZXN"

def thing():
    for letter in a:
        if letter not in letters:
            return "NO"
    return "YES"

print(thing())