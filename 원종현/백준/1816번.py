N=int(input())
t=[0,0]+[1]*(1000001)
so=[]
for i in range(2,1000001):
    if t[i]:
        so.append(i)
        for j in range(2*i,1000001,i):
            t[j]=0
for i in range(N):
    s=int(input())
    for j in so:
        if s%j==0:
            print("NO")
            break
    else:
        print("YES")