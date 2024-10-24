import math
W,I0,T=map(int,input().split())
D,I1,A=map(int,input().split())
w1,w2=W,W
I2=I0
for i in range(D):
    w1+=I1-(I0+A)
    w2+=I1-(I2+A)
    if abs(I1-(I2+A))>T:
        I2+=math.floor((I1-(I2+A))/2)

if w1<=0:
    print("Danger Diet")
else:
    print(w1,I0)

if w2<=0 or I2<=0:
    print("Danger Diet")
else:
    print(w2,I2,"YOYO" if I0-I2>0 else "NO")