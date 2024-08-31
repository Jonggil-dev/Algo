import heapq
def djikstra(s,e,maps):
    dij = [[0,1], [1,0], [0,-1], [-1,0]]
    dis = [[float("inf")]*len(maps[0]) for _ in range(len(maps))]
    pq = []
    heapq.heappush(pq,[0,s[0],s[1]])
    dis[s[0]][s[1]] = 0

    while pq:
        w, ci, cj = heapq.heappop(pq)
        if ci==e[0] and cj==e[1]:
            return w
        if dis[ci][cj] >= w:
            for d in dij:
                ni, nj = ci+d[0], cj+d[1]
                new_w = w+1
                if 0<=ni<len(maps) and 0<=nj<len(maps[0]) and maps[ni][nj] != "X":
                    if dis[ni][nj] > new_w:
                        dis[ni][nj] = new_w
                        heapq.heappush(pq,[new_w,ni,nj])
    return False

def solution(maps):
    answer = 0
    start, end, lever = [],[],[]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                start = [i,j]
            elif maps[i][j] == "E":
                end = [i,j]
            elif maps[i][j] == "L":
                lever = [i,j]
    
    first = djikstra(start, lever, maps)
    if not first:
        return -1
    second = djikstra(lever, end, maps)
    if not second:
        return -1
    return first + second
