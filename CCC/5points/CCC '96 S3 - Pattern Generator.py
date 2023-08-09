a = int(input())
samples = [list(map(int, input().split(" "))) for i in range(a)]

def printSolutions(n, k, curr):
    if n == 0:
        if k == 0:
            print(curr)
        return
    if k != 0:
        printSolutions(n-1, k-1, curr + '1')
    printSolutions(n-1, k, curr + '0')
    

for count, sample in enumerate(samples):
    n, k = sample
    print("The bit patterns are")
    printSolutions(n, k, '')
    if count != len(samples) - 1:
        print('')
