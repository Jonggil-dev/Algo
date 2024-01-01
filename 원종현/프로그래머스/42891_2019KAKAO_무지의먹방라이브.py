from collections import deque
def solution(food_times, k):
    answer = 0
    q=deque(sorted(food_times))
    d=0
    if sum(food_times)<=k:
        return -1
    while True:
        tot_food=len(q)
        if k<tot_food:
            break
        if q[0]-d>k//tot_food:
            k-=(k//tot_food)*tot_food
            d+=(k//tot_food)
        else:
            k-=(q[0]-d)*tot_food
            d+=(q[0]-d)
            now=q.popleft()
            while now==q[0]:
                q.popleft()
    for i in range(len(food_times)):
        if food_times[i]>d:
            k-=1
        if k<0:
            answer=i+1
            break
    return answer
