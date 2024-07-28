N=int(input())
li=list(map(int,input().split()))
r1,r2=set(),set()
for i in li:
    if i in r1 and i not in r2:
        r2.add(i)
    elif i not in r1:
        r1.add(i)
print(len(r1)+len(r2))