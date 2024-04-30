N,L=map(int,input().split())
li=list(map(int,input().split()))
li.sort()

for i in li:
    if i<=L:
        L+=1
print(L)