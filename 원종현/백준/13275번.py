import sys
input=sys.stdin.readline
S='#'+'#'.join(input().strip())+'#'
li=[0]*(len(S))
r,p=0,0
for i in range(len(S)):
    if i<=r:
        li[i]=min(li[2*p-i],r-i)
    while i-li[i]-1>=0 and i+li[i]+1<len(S) and S[i-li[i]-1]==S[i+li[i]+1]:
        li[i]+=1
    if r<i+li[i]:
        r=i+li[i]
        p=i
print(max(li))