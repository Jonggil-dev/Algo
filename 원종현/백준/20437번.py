import sys
input=sys.stdin.readline

for _ in range(int(input())):
    W=input()
    K=int(input())
    check={}
    for i in range(len(W)):
        if W[i] in check:
            check[W[i]].append(i)
        else:
            check[W[i]]=[i]
    for i in check:
        if len(check[i])>=K:
            break
    else:
        print(-1)
        continue
    st=1
    end=10000
    for i in check:
        for j in range(len(check[i])-K+1):
            now=check[i][j+K-1]-check[i][j]+1
            st=max(st,now)
            end=min(end,now)
    print(end,st)
