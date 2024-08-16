from collections import deque
def solution(n, wires):
    answer = 100
    for i in range(len(wires)):
        dic = {i:[] for i in range(1,n+1)}
        for j in range(len(wires)):
            if i != j:
                a, b = wires[j]
                dic[a].append(b)
                dic[b].append(a)
        
        v = []
        q = deque([1])
        while q:
            x = q.popleft()
            v.append(x)
            for y in dic[x]:
                if y not in v:
                    q.append(y)
                    
        if answer > abs(n-2*len(v)):
            answer = abs(n-2*len(v))
    return answer
