## 2회독 풀이로 참고하기 -> merge부분 제일 최적화 됨

def solution(commands):
    global excels, parents
    
    answer = []
    excels = [[0] * 51 for _ in range(51)]
    parents = [[(i, j) for j in range(51)] for i in range(51)]
    
    for command in commands:
        li = command.split()
        if li[0][:2] == "UP":
            if len(li) == 3:
                update3(li)
            else:
                update4(li)
                
        elif li[0][:2] == "ME":   
            merge(li)
            
        elif li[0][:2] == "UN":
            unmerge(li)
        else:
            answer.append(cprint(li))
    return answer

def find_parents(i, j):
    if parents[i][j] != (i, j):
        parents[i][j] = find_parents(parents[i][j][0], parents[i][j][1])
    return parents[i][j]
    
def update4(li):
    li[1], li[2] = int(li[1]), int(li[2])
    r, c = find_parents(li[1], li[2])
    excels[r][c] = li[3] 
    return

def update3(li):
    for r in range(51):
        for c in range(51):
            if excels[r][c] == li[1]:
                excels[r][c] = li[2]
    return

def merge(li):
    li[1], li[2], li[3], li[4] = int(li[1]), int(li[2]), int(li[3]), int(li[4])
    r1, c1 = find_parents(li[1], li[2])
    r2, c2 = find_parents(li[3], li[4])

    if (r1, c1) == (r2, c2):
        return
    
    if excels[r1][c1] and excels[r2][c2]:
        value = excels[r1][c1]
    else:
        if excels[r1][c1]:
            value = excels[r1][c1]
        else:
            value = excels[r2][c2]
            
    if r1 < r2:
        parents[r2][c2] = (r1, c1)
        excels[r1][c1] = value
        excels[r2][c2] = 0
    elif r2 < r1:
        parents[r1][c1] = (r2, c2)
        excels[r2][c2] = value
        excels[r1][c1] = 0
    else:
        if c1 < c2:
            parents[r2][c2] = (r1, c1)
            excels[r1][c1] = value
            excels[r2][c2] = 0
        else:
            parents[r1][c1] = (r2, c2)
            excels[r2][c2] = value
            excels[r1][c1] = 0
    return

def unmerge(li):
    for i in range(1, 51):
        for j in range(1, 51):
            find_parents(i, j)
    
    li[1], li[2] = int(li[1]), int(li[2])
    r, c = find_parents(li[1], li[2])
    value = 0
    
    if excels[r][c]:
        value = excels[r][c]
        excels[r][c] = 0
    
    for i in range(1, 51):
        for j in range(1, 51):
            if parents[i][j] == (r, c):
                parents[i][j] = (i, j)
    
    excels[li[1]][li[2]] = value
    return
    
def cprint(li):
    for i in range(1, 51):
        for j in range(1, 51):
            find_parents(i, j)
            
    li[1], li[2] = int(li[1]), int(li[2])
    r, c = find_parents(li[1], li[2])
    if not excels[r][c]:
        return "EMPTY"
    else:
        return excels[r][c]