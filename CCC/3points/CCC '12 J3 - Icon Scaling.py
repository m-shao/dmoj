k = int(input())
thing = ["*x*", " xx", "* *"]

for row in thing:
    for i in range(k):
        for col in range(3):
            print(row[col]*k, end="")
        print("")
    
