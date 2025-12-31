A,B=map(int,input().split())
A,B=min(A,B),max(A,B)
S=[1,2]
def get(x):
    a,b,t=0,0,0
    for i in range(len(S)):
        if S[i]<=x:
            continue
        else:
            a=i
            t=S[i-1]
            break
    b=x-t+1
    c=(len(S)+a-b)
    return a,b,c

for i in range(3,31625):
    S.append(2*(i-1)-1+S[i-2])

#print(S[-1])
#print(get(A),get(B),get(1),get(2))
Ax,Ay,Ac=get(A)
Bx,By,Bc=get(B)
if Ax==Bx: #o
    print(By-Ay)
elif Bx-Ax==1:
    if (A-Ax+1)%2==0: #o
        if abs(By-Ay) in [0,2]:
            print(2)
        else:
            print(2+min(abs(By-Ay-2),abs(By-Ay)))
    else: #o
        print(abs(By-Ay)+1+1)
else:
    p4=0
    tmp=0
    Acheck,Bcheck=(A-Ax+1)%2,(B-Bx+1)%2
    if Acheck==0 and Bcheck!=0:
        tmp+=1
    elif Acheck!=0 and Bcheck==0:
        tmp-=1
    p4=2*(Bx-Ax)+tmp
    if abs(Bc-Ac)<=(Bx-Ax):
        print(p4)
    else:
        print(p4+min(abs(By-Ay),abs(By-(Ay+2*(Bx-Ax-1)))))
# 1,2,5,10,17,26,37
#  1 3 5  7  9