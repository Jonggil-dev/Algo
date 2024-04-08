H,W=map(int,input().split())
li=list(map(int,input().split()))
r=0
for i in range(max(li)+1):
    c=0
    check=0
    for j in range(W):
        if not check and li[j]>=i:
            check=1

        elif check and li[j]<i:
            c+=1
            print(i,j)
        elif check and li[j]>=i:
            r+=c
            c=0

print(r)