import sys
input=sys.stdin.readline

N=int(input())
name={}
for i in range(N):
    tmp=input()
    if tmp in name:
        name[tmp]+=1
    else:
        name[tmp]=1
for i in range(N-1):
    tmp=input()
    if tmp in name:
        if not name[tmp]:
            del name[tmp]
        else:
            name[tmp]-=1
for k,v in name.items():
    if v==1:
        print(k)
        break