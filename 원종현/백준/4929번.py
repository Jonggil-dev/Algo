while True:
    li1=list(map(int,input().split()))
    if len(li1)==1 and li1[0]==0:
        break
    li1=li1[1:]
    li2=list(map(int,input().split()))[1:]
    g=set(li1)&set(li2)
    if len(li1)<len(li2):
        li1,li2=li2,li1
    a,b=[0],[0]
    tmp1,tmp2=0,0
    res=0
    for i in range(len(li1)):
        if li1[i] in g:
            a.append(i)
            #res+=li1[i]
    for i in range(len(li2)):
        if li2[i] in g:
            b.append(i)
    a.append(len(li1))
    b.append(len(li2))
    for i in range(len(a)-1):
        res+=max(sum(li1[a[i]:a[i+1]]),sum(li2[b[i]:b[i+1]]))
    print(res)