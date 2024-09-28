def func(N):
    li=[int(N[0]),int(N[:2]),int(N[:3])]
    for i in li:
        tmp=i
        new=''
        while len(new)<len(N):
            new+=str(tmp)
            if new==N:
                return i,tmp
            tmp+=1
    return N,N
print(*func(input()))