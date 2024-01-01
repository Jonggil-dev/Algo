'''
설계
1. 에러가 발생한 시간초가 음식의 총 갯수보다 크면 음식 1사이클이 돌고, 전체 각 음식 시간이 -1초가 됨
2. 싸이클이 돌지 못할 경우 에러 발생 까지 남은 시간초만큼 인덱스 계산해서 음식 추출하기
3. 싸이클이 돌다보면 시간초가 제일 작은 음식이 0이 되고 싸이클에서 빠지게 됨 이부분 고려해서 설계하기
4. 결국 제일 작은 시간을 가진 음식을 기준으로, 최소 음식 시간 * 남은 음식의 갯수 > k가 될 때까지 계속 비교하면 됨
'''
import heapq

def solution(food_times, k):

    #전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    answer = 0
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    food_length = len(food_times)
    q = []

    for i in range(food_length):
        heapq.heappush(q,(food_times[i],i+1))

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수 vs k 비교
    while sum_value + ((q[0][0] - previous ) *  food_length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * food_length
        food_length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x: x[1]) #음식의 번호 기준으로 정렬
    return result[(k-sum_value) % food_length][1]

print(solution([8,6,4], 15))