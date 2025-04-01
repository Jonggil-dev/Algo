for _ in range(int(input())):
    S=input().split()
    r=[]
    for i in S:
        t=0
        for j in i:
            t+=ord(j)-97
        r.append(t%27)
    r=''.join([chr(i+97) if 0<=i<26 else ' ' for i in r])
    print(S)
    print(r)
print(ord('a'),ord('z')-97)