import sys
li=bytearray(2**22)
s=''
while True:
    S=sys.stdin.read(1)
    if S.isnumeric():
        s+=S
    else:
        N=int(s)
        d=N//8
        r=N%8
        if not li[d]&(1<<r):
            print(N,end=" ")
            li[d]|=1<<r
        s=''
        if S!=" ":
            break