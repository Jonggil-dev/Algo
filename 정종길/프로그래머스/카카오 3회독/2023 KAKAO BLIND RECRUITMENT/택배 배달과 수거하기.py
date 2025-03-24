'''
1. 배달이던 수거던 어짜피 가장 먼 곳까지는 가야 됨
 -> 배달의 경우는 꽉 채워 출발해서 가는 길에 다 뿌려 주면 됨
 -> 수거의 경우 오는 길에 다 수집해서 오면 됨
2. 가장 먼 곳을 계속 왕복 하면서, 배달 수거를 지워가기
'''

def solution(cap, n, deliveries, pickups):
    answer = 0
    d = p = n - 1
    
    while d >= 0 or p >= 0:
        cnt = cap
        while d >= 0 and not deliveries[d]:
            d -= 1
        while p >= 0 and not pickups[p]:
            p -= 1
    
        answer += max(d + 1, p + 1) * 2
        
        d = act(deliveries, d, cap)
        p = act(pickups, p, cap)
        
    return answer

def act(li, here, cap):
    while here >= 0:
        if cap <= li[here]:
            li[here] -= cap
            return here
        else:
            cap -= li[here]
            li[here] = 0
            here -= 1
    return here