import sys
S=list(input())
T=list(input())

def func(t):
    if t==S:
        print(1)
        sys.exit()
    if len(t)==0:
        return
    if t[-1]=='A':
        func(t[:-1])
    if t[0]=='B':
        func(t[1:][::-1])
func(T)
print(0)