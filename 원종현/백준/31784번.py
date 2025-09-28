N,K=map(int,input().split())
li=list(input())
for i in range(N):
    now=91-ord(li[i])
    if i==N-1:
        if K:
            tmp=ord(li[i])+(K%26)
            if tmp>=91:
                tmp-=26
            li[i]=chr(tmp)
    else:
        if now==26:
            continue
        if now<=K:
            li[i]='A'
            K-=now
print(''.join(li))