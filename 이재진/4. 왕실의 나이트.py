N = input()
tmp = ord(N[0]) - 96
now = [tmp, int(N[1])]
res = 0
for i in [2,-2]:
    for j in [1,-1]:
        if 1 <= now[0]+i <= 8 and 1 <= now[1]+j <= 8:
            res += 1
for i in [1,-1]:
    for j in [2,-2]:
        if 1 <= now[0]+i <= 8 and 1 <= now[1]+j <= 8:
            res += 1
print(res)