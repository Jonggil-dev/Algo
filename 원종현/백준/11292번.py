while True:
    li=[]
    N=int(input())
    if N==0:
        break
    for i in range(N):
        S=input().split()
        S[1]=float(S[1])
        li.append(S)
    tmp=max(li,key=lambda x:x[1])[1]
    for i in li:
        if i[1]==tmp:
            print(i[0],end=' ')
    print()