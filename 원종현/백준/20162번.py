import sys
input=sys.stdin.readline

N=int(input())

s=int(input())
dp1,dp2=[s],[s]

for _ in range(N-1):
    s=int(input())
    li=[]
    for i,v in enumerate(dp1):
        if v<s:
            li.append(dp2[i])
    dp1.append(s)
    if li:
        dp2.append(max(li)+s)
    else:
        dp2.append(s)
print(max(dp2))