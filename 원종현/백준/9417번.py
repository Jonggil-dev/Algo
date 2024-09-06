N=int(input())
li=[list(map(int,input().split())) for _ in range(N)]

def func(a,b):
    while b>0:
        a,b=b,a%b
    return a

for i in li:
    tmp=[]
    for j in range(len(i)):
        for k in range(j,len(i)):
            if j!=k:
                tmp.append(func(i[j],i[k]))
    print(max(tmp))