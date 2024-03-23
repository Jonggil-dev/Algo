def solution(park, routes):
    import copy
    mi, mj = len(park), len(park[0])
    for i in range(mi):
        if 'S' in park[i]:
            for j in range(mj):
                if park[i][j] == 'S':
                    now = [i,j]
    
    dic = {'E':[0,1] ,'W':[0,-1], 'S':[1,0], 'N':[-1,0] }
    for i in routes:
        d, num = i.split()
        flag = 1
        tmp = copy.deepcopy(now)
        for _ in range(int(num)):
            ni = tmp[0] + dic[d][0]
            nj = tmp[1] + dic[d][1]
            if 0<=ni<mi and 0<=nj<mj and park[ni][nj] != 'X':
                tmp = [ni,nj]
            else:
                flag = 0
                break
        if flag:
            now = tmp
        
    answer = now
    return answer
