n = int(input())
messages = [input() for i in range(n)]

for message in messages:
    for word in message.split(" "):
        if len(word) == 4:
            print("****", end=" ")
        else:
            print(word, end=" ")
    print("")