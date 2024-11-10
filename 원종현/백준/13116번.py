import math,sys
input=sys.stdin.readline
def func(n):
    return math.floor(math.log2(n))
for i in range(int(input())):
    a,b=map(int,input().split())
    while True:
        A,B=func(a),func(b)
        if A>B:
            a//=2
        elif A<B:
            b//=2
        else:
            break
    while a!=b:
        a//=2
        b//=2
    print(a*10)