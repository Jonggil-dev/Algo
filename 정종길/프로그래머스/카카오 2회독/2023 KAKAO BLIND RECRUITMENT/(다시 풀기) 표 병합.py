def solution(commands):
    global excel, answer, parents
    
    answer = []
    excel = [[0] * 51 for _ in range(51)]
    parents =[[(i, j) for j in range(51)] for i in range(51)]
    
    for command in commands:
        li = command.split()
        if li[0] == "UPDATE":
            if len(li) == 4:
                update_rc(int(li[1]), int(li[2]), li[3])
            else:
                update_v(li[1], li[2])
                
        elif li[0] == "MERGE":
            merge(int(li[1]), int(li[2]), int(li[3]), int(li[4]))
            
                
        elif li[0] == "UNMERGE":
            unmerge(int(li[1]), int(li[2]))
            
        else:
            pprint(int(li[1]), int(li[2]))

    return answer

def find_parents(r, c):
    global parents
    
    if parents[r][c] != (r, c):
        parents[r][c] = find_parents(parents[r][c][0], parents[r][c][1])
    
    return parents[r][c]

def merge(r1, c1, r2, c2):
    global parents, excel
    
    pr1, pc1 = find_parents(r1, c1)
    pr2, pc2 = find_parents(r2, c2)
    parents[pr2][pc2] = (pr1, pc1)
    
    if (pr1, pc1) == (pr2, pc2):
        return
    
    if excel[pr1][pc1] and excel[pr2][pc2]:
        excel[pr2][pc2] = 0
           
    elif excel[pr2][pc2]:
        excel[pr1][pc1] = excel[pr2][pc2]
        excel[pr2][pc2] = 0
        
    elif excel[pr1][pc1]:
        excel[pr2][pc2] = 0

    return

def unmerge(r, c):
    global parents, excel
    
    for i in range(51):
        for j in range(51):
            find_parents(i, j)
                
    pr, pc = find_parents(r, c)
    v = excel[pr][pc]
        
    for i in range(51):
        for j in range(51):
            if parents[i][j] == (pr, pc):
                parents[i][j] = (i, j)
                
    excel[pr][pc] = 0
    excel[r][c] = v
    
    return 

def update_rc(r, c, v):
    global excel, parents
    
    pr, pc = find_parents(r,c)
    
    excel[pr][pc] = v
    return

def update_v(v1, v2):
    global excel
    
    for i in range(51):
        for j in range(51):
            if excel[i][j] == v1:
                excel[i][j] = v2
    return

def pprint(r, c):
    global excel, answer
    pr, pc = find_parents(r, c)
    
    if not excel[pr][pc]:
        answer.append("EMPTY")
    else:
        answer.append(excel[pr][pc])
    return