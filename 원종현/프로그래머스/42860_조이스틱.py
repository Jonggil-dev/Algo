def solution(name):
    def calc(a,b):
        if a>b:a,b=b,a
        return min(b-a,a+len(name)-b)
    def func(now,visit,v):
        nonlocal min_val
        if v>min_val:
            return
        if len(visit)==N:
            min_val=min(min_val,v)
            return
        for i in range(N):
            right=(now+i+N)%N
            if right not in visit:
                func(right,visit+[right],v+calc(check[now],check[right]))
                break
        for i in range(N):
            left=(now-i+N)%N
            if left not in visit:
                func(left,visit+[left],v+calc(check[now],check[left]))
                break
    min_val=1000
    name=list(name)
    for i in range(len(name)):
        name[i]=min(abs(ord(name[i])-ord('A')),(ord('Z')-ord(name[i])+1))
    answer=sum(name)
    if not name[0]:
        name[0]=1
    c=0
    check={}
    for i in range(len(name)):
        if name[i]:
            check[c]=i
            c+=1
    nodes=[i for i in range(len(check))]
    N=len(nodes)
    func(0,[0],0)
    return answer+min_val