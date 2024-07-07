from collections import deque
def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)//2+1):
        str_short = ""
        q = deque()
        now = 0
        while now < len(s):
            tmp = ""
            for j in range(i):
                tmp += s[now]
                now += 1
                if now >= len(s):
                    break
            q.append(tmp)
        while q:
            now = q.popleft()
            cnt = 1
            while q and now == q[0]:
                q.popleft()
                cnt += 1
            if cnt != 1:
                str_short += str(cnt)+now
            else:
                str_short += now
        if answer > len(str_short):
            answer = len(str_short)
        
            
            
            
    return answer
