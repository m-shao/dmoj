n = int(input())
nums = [int(input()) for i in range(n)]

for num in nums:
    total = 1
    for i in range(2, num - 1):
        if num % i == 0:
            total += i
    if total > num:
        print(f"{num} is an abundant number.")
    elif total < num:
        print(f"{num} is a deficient number.")
    else:
        print(f"{num} is a perfect number.")