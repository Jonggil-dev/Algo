import sys
input=sys.stdin.readline
N,K=map(int,input().split())
r=[]
for i in range(N):
    a,b,c,d=input().split()
    r.append((a,b,int(c),int(d)))
c={}
r.sort(key=lambda x:(-x[2],x[3]))
co=0
for i in range(N):
    if r[i][0] not in c:
        print(r[i][1])
        co+=1
        c[r[i][0]]=1
    if co==K:
        break
