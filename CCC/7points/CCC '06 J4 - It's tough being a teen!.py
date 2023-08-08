rules = [[1,7], [1,4], [2,1], [3,4], [3,5]]

while rules[-1] != [0,0]:
    rules.append([int(input()), int(input())])
    
rules = rules[:-1]

final = []

for rule in rules:
    if rule[1] not in final:
        final.append(rule[0])
        final.append(rule[1])
    else:
        if rule[0] in final:
            final.remove(rule[0])
        ind = final.index(rule[1])
        final.insert(ind, rule[0])
print(final) 
        