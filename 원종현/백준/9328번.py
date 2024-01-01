import sys
from collections import deque
d=[0,0,1,-1]
input=sys.stdin.readline

def bfs(visited):
    global ans

    q = deque([[0, 0]])
    visited[0][0] = True
    while q:
        r,c=q.popleft()
        for i in range(4):
            nr,nc=r+d[i],c+d[3-i]
            if nc<0 or nc>=w+2 or nr<0 or nr>=h+2 or miro[nr][nc]=='*' or visited[nr][nc]:
                continue
            if 'A' <= miro[nr][nc] <= 'Z':
                if chr(ord(miro[nr][nc]) + 32) not in key:
                    continue
            elif 'a' <= miro[nr][nc] <= 'z':  # 만약 소문자이고
                if miro[nr][nc] not in key:  # 아직 키에 없다면
                    key[miro[nr][nc]] = True  # 해당 키를 저장후
                    visited = [[False] * (w + 2) for _ in range(h + 2)]
            elif miro[nr][nc] == "$" and (nr, nc) not in visited2:
                ans+=1
                visited2.append((nr, nc))
            visited[nr][nc]=True  # 방문처리
            q.append([nr,nc])  # 다음 위치를 큐에 삽입

for _ in range(int(input())):
    h,w=map(int, input().split())

    miro=['.'+input()+'.'for _ in range(h)]
    miro=['.'*(w+2)]+miro+['.'*(w+2)]
    visited=[[False]*(w+2) for _ in range(h+2)]
    key={}
    visited2=[]

    for i in input():
        if i.isalpha():  # 만약 알파벳이면
            key[i]=True  # 키로 저장

    ans = 0
    bfs(visited)
    print(ans)