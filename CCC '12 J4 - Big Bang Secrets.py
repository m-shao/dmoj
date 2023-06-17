k = int(input())
scram = input()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

newWord = ""
for ind, letter in enumerate(scram):
    s = 3*(ind + 1) + k
    rotationFactor = (alphabet.index(letter) - s)
    newWord += alphabet[rotationFactor]
    
print(newWord)