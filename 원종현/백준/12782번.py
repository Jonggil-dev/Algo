for _ in range(int(input())):
    N,M=map(str,input().split())
    a,b=0,0
    for i in range(len(N)):
        if N[i]!=M[i]:
            if M[i]=='1':
                a+=1
            else:
                b+=1
    print(max(a,b))