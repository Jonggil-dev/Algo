N=int(input())
li=list(map(int,input().split()))
if N==1:
    print('A')
elif N==2:
    if li[0]==li[1]:
        print(li[0])
    else:
        print('A')
else:
    check=0
    if li[0]==li[1]:
        a=0
    else:
        a=(li[2]-li[1])//(li[1]-li[0])
    b=li[1]-li[0]*a
    for i in range(N-1):
        tmp=li[i]*a+b
        if tmp!=li[i+1]:
            print('B')
            check=1
            break
    if not check:
        print(li[-1]*a+b)
