n=int(input())
res=0

for _ in range(n):
    s=[]
    li=list(input())
    for i in li:
        if not len(s):
            s.append(i)
        elif s[-1] == i:
            s.pop(-1)
        else:
            s.append(i)

    if not len(s):
        res+=1 

print(res)