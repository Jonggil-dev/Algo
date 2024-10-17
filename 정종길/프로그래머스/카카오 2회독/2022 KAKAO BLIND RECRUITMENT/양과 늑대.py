from collections import deque

def solution(info, edges):
    answer = 0
    
    n = len(info)
    graph = [[] for _ in range(n)]
    
    for s, e in edges:
        graph[s].append(e)

    
    q = deque([(1, 0, graph[0])])

    while q:
        s, w, theres = q.popleft()
        
        for there in theres:
            if info[there]:
                if w + 1 >= s:
                    continue
                else:
                    ntheres = theres[:]
                    ntheres.remove(there)
                    q.append((s, w + 1, ntheres + graph[there]))
            else:
                ntheres = theres[:]
                ntheres.remove(there)
                q.append((s + 1, w, ntheres + graph[there]))
        answer = max(answer, s)
    return answer