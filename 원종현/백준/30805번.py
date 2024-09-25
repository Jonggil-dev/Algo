N=int(input())
A=list(map(int,input().split()))
M=int(input())
B=list(map(int,input().split()))

def func(li1,li2,r):
    if not li1 or not li2:
        return r

    max1,max2=max(li1),max(li2)
    idx1,idx2=li1.index(max1),li2.index(max2)
    if max1==max2:
        r.append(max1)
        return func(li1[idx1+1:],li2[idx2+1:],r)
    elif max1>max2:
        li1.pop(idx1)
        return func(li1,li2,r)
    else:
        li2.pop(idx2)
        return func(li1,li2,r)

t=func(A,B,[])
print(len(t))
if t:
    print(*t)