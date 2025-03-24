def solution(n, w, num):
    answer = 1
    posts = []

    level = ((n - 1) // w) + 1
    
    for i in range(1, level + 1):
        row = []
        if i == level:
            if i % 2 == 1:
                for j in range(w * (i - 1) + 1, n + 1):
                    row.append(j)
            else:
                for j in range(n, w * (i - 1), -1):
                    row.append(j)
                    
            if len(row) < w:
                if i % 2 == 1:
                    row = row + [-1] * (w - len(row))                
                else:
                    row = [-1] * (w - len(row)) + row     
        else: 
            if i % 2 == 1:
                for j in range(w * (i - 1) + 1, w * i + 1):
                    row.append(j)
            else:
                for j in range(w * i, w * (i - 1), -1):
                    row.append(j)
            
        posts.append(row)
        
    for i in range(level):
        for j in range(w):
            if posts[i][j] == num:
                while i < level - 1:
                    i += 1
                    if posts[i][j] == -1:
                        return answer
                    else:
                        answer += 1
                        
                return answer           