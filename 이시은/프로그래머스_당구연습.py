# 프로그래머스 Lv2 당구연습
def solution(m, n, startX, startY, balls):
    answer = []
    for targetX, targetY in balls:
        tmp = find_shortest(startX, startY, targetX, targetY, m, n)
        answer.append(tmp)

    return answer

def find_shortest(a, b, c, d, m, n):
    result = float("inf")
    # 같은 축(x or y 값이 같다)에 있는 경우 : 
    # x 값이 같은 경우: c값이 0과 m중 어디에 가까운지 판단 -> 0이 가까우면 (a, b), (-c, d) 거리 구하기 / n이 가까우면 (a, b), (m+c, d) 거리 구하기
    if a == c:
        if c <= m-c:
            dist = (a+c)**2 + (d-b)**2

        else:
            dist = (a-(2*m-c))**2 + (d-b)**2

        if b < d:
            return min(dist, (b+d)**2)
        else:
            return min(dist, (2*n-b-d)**2)
    # y 값이 같은 경우: d값이 0과 n중 어디에 가까운지 판단 -> 0이 가까우면 (a, b), (c, -d) 거리 구하기 / n이 가까우면 (a, b), (c, n+d) 거리 구하기
    if b == d:
        if d <= n-d:
            dist = (b+d)**2 + (a-c)**2

        else:
            dist = (b-(2*n-d))**2 + (a-c)**2

        if a < c:
            return min(dist, (a+c)**2)
        else:
            return min(dist, (2*m-a-c)**2)
    # 아닌 경우: 네 면에 모두 반사시켜보고 최솟값을 result에 담기
    # x축 반사
    print("e")
    dist = ((a-c)**2 + (b+d)**2)
    result = min(result, dist)
    # y축 반사
    dist = ((a+c)**2 + (b-d)**2)
    result = min(result, dist)
    # x=m에 반사
    dist = ((a-(2*m-c))**2 + (b-d)**2)
    result = min(result, dist)
    # y=n에 반사
    dist = ((a-c)**2 + (b-(2*n-d))**2)
    result = min(result, dist)
    return result
    
