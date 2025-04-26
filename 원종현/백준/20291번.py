import sys
input=sys.stdin.readline

N=int(input())
d={}
for i in range(N):
    _,c=input().rstrip().split('.')
    if c in d:
        d[c]+=1
    else:
        d[c]=1
li=[[k,v] for k,v in d.items()]
li.sort(key=lambda x:x[0])
for k,v in li:
    print(k,v)