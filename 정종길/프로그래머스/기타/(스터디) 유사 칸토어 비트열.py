'''
1. n단계 유사 칸토어 비트열을 S(n) 이라고 한다면
2. S(n) = S(n-1) + S(n-1) + 0무더기 + S(n-1) + S(n-1) 임을 알아야 됨
3. 즉, S(n), S(n-1), S(n-2) ... 등 각 단계의 유사 칸토어 비트열을 5등분 하면 가운데가 0무더기 파트가 됨 
-> 이거는 그냥 3단계 까지 그려보면 이해 됨

4. 그래서 결국 S(n) 단계를 5등분 한뒤 l, r의 구간이 5등분 중에서 가운데 파트에 위치한다면 해당 위치는 0이라는 소리 -> n이 1단계 까지 재귀로 파고 갔는데도 만약에 0에 해당이 안하면 해당 위치는 1이라는 뜻

5. 재귀 연산횟수 
-> n = 20 단계 이면서 모든 구간을 다 쪼갠다고 했을 때
-> 20단계는 5분할 연산 1번 -> 2 ^ 0
-> 19단계는 5분할 연산 4번 -> 2 ^ 2
-> 18단계는 5분할 연산 4번 * 4 -> 2 ^ 3
-> 대충 2 ^ 19  + 2 ^ 18 -> (2 ^ 20) - 1 = 100만 번 

6. 아래 풀이는
전체 l, r 구간을 고정해두고 그 내부에 해당하는 파트를 계속 쪼개서 확인하는 방식 -> 재귀 함수 짤 때 헷갈림
'''


def solution(n, l, r):
    length = 5 ** n
    return find_one(1, length, l, r)

def find_one(part_left, part_right, check_l, check_r):
    
    if part_right < check_l or check_r < part_left:
        return 0
    
    if part_left == part_right:
        return 1
    
    cnt = 0
    ran = (part_right - part_left + 1) // 5
    
    for i in range(5):
        if i == 2:
            continue
        cnt += find_one(part_left + i * ran, part_left + (i + 1) * ran - 1, check_l, check_r)
    
    return cnt