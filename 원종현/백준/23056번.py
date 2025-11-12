import sys
input=sys.stdin.readline

N,M=map(int,input().split())
li=[[] for _ in range(N+1)]
while True:
    a,b=input().rstrip().split()
    if a=='0' and b=='0':
        break
    a=int(a)
    if len(li[a])<M:
        li[a].append(b)

for i in range(1,N+1):
    li[i].sort()
    li[i].sort(key=lambda x:len(x))

for i in range(1,N+1):
    if i%2:
        for j in range(len(li[i])):
            print(i,li[i][j])
    else:
        continue
for i in range(1,N+1):
    if not i%2:
        for j in range(len(li[i])):
            print(i,li[i][j])
    else:
        continue