plain = input()
cipher = input()
message = input()
finalMessage = ""

realAlphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
fakeAlphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

dic1={}

for real, fake in zip(plain, cipher):
    dic1[fake] = real
    if real in realAlphabet:
        realAlphabet.remove(real)
    if fake in fakeAlphabet:
        fakeAlphabet.remove(fake)
if len(realAlphabet) == 1:
    dic1[fakeAlphabet[0]] = realAlphabet[0]
    

for letter in message:
    finalMessage += dic1[letter] if letter in dic1 else "."

print(finalMessage)
