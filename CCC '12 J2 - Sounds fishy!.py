readings = [int(input()) for i in range(4)]

if readings[0] < readings[1] and readings[1] < readings[2] and readings[2] < readings[3]:
    print("Fish Rising")
elif readings[0] > readings[1] and readings[1] > readings[2] and readings[2] > readings[3]:
    print("Fish Diving")
elif readings[0] == readings[1] and readings[1] == readings[2] and readings[2] == readings[3]:
    print("Fish At Constant Depth")
else:
    print("No Fish")