import sys
input=sys.stdin.readline

def func(li,D,parent):
    if not li:
        return
    if not parent:
        parent=li.pop()
        D[parent]=[]
        if parent=='nil':
            return
        func(li,D,parent)
    else:
        for _ in range(2):
            if not li:
                continue
            next=li.pop()
            if next=='nil':
                continue
            D[parent].append(next)
            D[next]=[]
            func(li,D,next)

for _ in range(int(input())):
    A=input().rstrip().split()[:-1]
    B=input().rstrip().split()[:-1]
    s1,s2=A[-1],B[-1]
    D1,D2={},{}
    func(A,D1,'')
    func(B,D2,'')
    li1=sorted([[k,sorted(v)]  for k,v in D1.items()])
    li2=sorted([[k,sorted(v)] for k,v in D2.items()])
    res='true'
    if li1!=li2:
        res='false'
    print(res)