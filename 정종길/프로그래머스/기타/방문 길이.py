def solution(dirs):
    i,j = (0, 0)
    visited = set()
    
    for d in dirs:
        if d == "L":
            di, dj = (0, -1)
        elif d == "R":
            di, dj = (0, 1)
        elif d == "U":
            di, dj = (1, 0)
        else:
            di, dj = (-1, 0)
            
        ni, nj = i + di, j + dj
        if -5 <= ni <= 5 and -5 <= nj <= 5:
            root = [(i, j), (ni, nj)]
            root.sort(key = lambda x : (x[0], x[1]))
            visited.add(tuple(root))
            i, j = ni, nj

    return len(visited)