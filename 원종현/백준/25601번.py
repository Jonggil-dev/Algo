import sys
input=sys.stdin.readline


def func(A,B):
    parent=A
    while True:
        try:
            parent=d[parent]
            if parent==B:
                return 1
        except:
            return 0

N=int(input())
d={}
for i in range(N-1):
    A,B=input().split()
    d[A]=B
A,B=input().split()
print(func(A,B)|func(B,A))