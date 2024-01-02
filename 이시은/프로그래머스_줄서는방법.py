# 프로그래머스 줄 서는 방법

import math

def solution(n, k):
    answer = []
    org = list(range(1, n+1))
    idx = 1
    # i = 0
    while k > 0:
        # print(i, '번째:', n, k, idx, org, answer)
        if k - idx * math.factorial(n-1) > 0:
            idx += 1
        elif k - idx * math.factorial(n-1) < 0:
            k -= (idx-1) * math.factorial(n-1)
            tmp = org[idx-1]
            answer.append(tmp)
            org.remove(tmp)
            idx = 1
            n -= 1
        else:
            tmp = org[idx-1]
            answer.append(tmp)
            org.remove(tmp)
            answer.extend(sorted(org, reverse=True))
            break
    # i+=1
    return answer


print(solution(3, 5))
print(solution(4, 10))