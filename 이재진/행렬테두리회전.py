def solution(rows, columns, queries):
    answer = []
    ls = []
    for r in range(rows):
        tmp = []
        for j in range(columns):
            tmp.append(r*columns + j+1)
        ls.append(tmp)
    dxy = [[0,1], [1,0], [0,-1], [-1,0]]
    for q in queries:
        start_x, start_y, end_x, end_y = q[0]-1, q[1]-1, q[2]-1, q[3]-1
        dir = 0
        tmp_ls = []
        idx_ls = []
        nx, ny = start_x, start_y
        cnt = 0
        while True:          
            cx, cy = nx, ny
            nx, ny = cx + dxy[dir][0], cy + dxy[dir][1]
            if not (start_x <= nx <= end_x) or not (start_y <= ny <= end_y):
                dir = (dir+1) % 4
                nx, ny = cx + dxy[dir][0], cy + dxy[dir][1]
            
            tmp_ls.append(ls[cx][cy])
            idx_ls.append([cx,cy])
            cnt += 1
            if nx == start_x and ny == start_y:
                break
                
        answer.append(min(tmp_ls))
        
        tmp_ls.insert(0, tmp_ls.pop())
        for i in range(len(tmp_ls)):
            di, dj = idx_ls[i]
            ls[di][dj] = tmp_ls[i]
    
    return answer
