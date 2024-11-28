def algo(start, end):
    ci, cj = start[0], start[1]
    dis = [[ci, cj]]
    if ci > end[0]:
        while ci != end[0]:
            ci -= 1
            dis.append([ci,cj])
    elif ci < end[0]:
        while ci != end[0]:
            ci += 1
            dis.append([ci,cj])
            
    if cj > end[1]:
        while cj != end[1]:
            cj -= 1
            dis.append([ci,cj])
    elif cj < end[1]:
        while cj != end[1]:
            cj += 1
            dis.append([ci,cj])
    
    return dis
    
def solution(points, routes):
    answer = 0
    ls = []
    n = 0
    for r in routes:
        tmp = []
        for i in range(len(r)-1):
            dis = algo(points[r[i]-1], points[r[i+1]-1])
            if i == 0:
                tmp.extend(dis)
            else:
                tmp.extend(dis[1:])
        ls.append(tmp)
        if n < len(tmp):
            n = len(tmp)
    
    for i in range(n):
        dic = {}
        for j in ls:
            if i < len(j):
                if str(j[i]) not in dic:
                    dic[str(j[i])] = 1
                else:
                    dic[str(j[i])] += 1
        for k in dic.keys():
            if dic[k] != 1:
                answer += 1
    return answer
