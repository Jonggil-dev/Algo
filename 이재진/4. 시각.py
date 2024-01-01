N = int(input())
res = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            tmp = str(i)+str(j)+str(k)
            if "3" in tmp:
                res += 1
print(res)