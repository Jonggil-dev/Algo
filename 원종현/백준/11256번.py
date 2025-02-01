for i in range(int(input())):
    J,N=map(int,input().split())
    li=[]
    for j in range(N):
        a,b=map(int,input().split())
        li.append(a*b)
    li.sort(reverse=True)
    res=0
    for j in range(len(li)):
        J-=li[j]
        res+=1
        if J<=0:
            break
    print(res)