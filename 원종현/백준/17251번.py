N=int(input())
li=list(map(int,input().split()))
mv=max(li)
tmp=[]
c=0
for i in li:
    if i==mv:
        tmp.append(c)
    c+=1

if len(tmp)>1:
    st,end=tmp[0],tmp[-1]
    B=st
    X=end-st
    R=N-1-B-X
else:
    B=tmp[0]
    R=N-1-B

if B>R:
    print('B')
elif R>B:
    print('R')
else:
    print('X')