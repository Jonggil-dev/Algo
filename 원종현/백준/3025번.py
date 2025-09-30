import sys
input=sys.stdin.readline

def calc(idx,x,y):
    while x<R:
        if x+1!=R:
            if li[x+1][y]=='.':
                x+=1
            elif li[x+1][y]=='X':
                break
            else:
                if 0<=y-1<C and li[x][y-1]=='.' and li[x+1][y-1]=='.':
                    x+=1
                    y-=1
                elif 0<=y+1<C and li[x][y+1]=='.' and li[x+1][y+1]=='.':
                    x+=1
                    y+=1
                else:
                    break
        else:
            break
        stk[idx].append((x,y))
    return x,y
R,C=map(int,input().split())
li=[list(input().rstrip()) for _ in range(R)]
visit=[[0]*(C) for _ in range(R)]
stk=[[]*R for _ in range(C)]

for i in range(C):
    x,y=0,i
    stk[i].append((x,y))
    calc(i,0,i)

N=int(input())
for c in range(N):
    now=int(input())-1
    if li[stk[now][-1][0]][stk[now][-1][1]]=='.':
        x,y=stk[now].pop()
        li[x][y]='O'
        if stk[now]:
            x,y=calc(now,stk[now][-1][0],stk[now][-1][1])
    else:
        x,y=stk[now].pop()
        while li[x][y]!='.':
            x,y=stk[now].pop()
        x,y=calc(now,x,y)
        li[x][y]='O'
        calc(now,stk[now][-1][0],stk[now][-1][1])

for i in li:
    print(*i,sep='')