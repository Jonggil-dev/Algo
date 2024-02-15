import sys
input=sys.stdin.readline
def check(team):
    tmp=color
    for i in range(len(team)):
        if 0 in tmp and team[i:] in name:
            return 1
        if team[i] not in tmp:
            return 0
        tmp=tmp[team[i]]

C,N=map(int,input().rstrip().split())

color={}
for i in range(C):
    tmp=color
    for j in input().rstrip():
        if j not in tmp:
            tmp[j]={}
        tmp=tmp[j]
    tmp[0]=1

name={input().rstrip() for _ in range(N)}

print(color)
for _ in range(int(input())):
    team=input().rstrip()
    if check(team):
        print("Yes")
    else:
        print("No")