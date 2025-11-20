import sys
input=sys.stdin.readline
N=int(input())
S=input().rstrip()
a,b,c,d=S.count("A"),S.count("C"),S.count("G"),S.count("T")
res=min(a,b,c,d)
print(res)
if a==res:
    print('A'*N)
elif b==res:
    print('C'*N)
elif c==res:
    print('G'*N)
else:
    print('T'*N)