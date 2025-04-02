while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    if (c-a)%b:
        print("X")
    else:
        if (b>0 and c<a) or (b<0 and c>a):
            print("X")
        else:
            print((c-a)//b+1)
