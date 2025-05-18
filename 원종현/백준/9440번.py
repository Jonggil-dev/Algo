import sys
input=sys.stdin.readline

while True:
    li=list(map(int,input().split()))

    if li[0]==0:
        break
    else:
        li=sorted(li[1:])
        c=li.count(0)
        li=li[c:]
        a,b='',''
        for i in range(len(li)):
            if i%2==0:
                a+=str(li[i])
            else:
                b+=str(li[i])
        c_a,c_b=c//2,c//2
        if len(a)>len(b):
            c_b+=c%2
        else:
            c_a+=c%2
        a=a[0]+('0'*c_a)+a[1:]
        b=b[0]+('0'*c_b)+b[1:]
        print(int(a)+int(b))