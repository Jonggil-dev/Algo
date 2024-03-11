from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([])
    i = 0
    answer = 0
    now_weight = 0

    while i < len(truck_weights):
        answer += 1
        if now_weight + truck_weights[i] <= weight and len(bridge) + 1 <= bridge_length:
            bridge.append([truck_weights[i], 0])
            now_weight += truck_weights[i]
            i += 1

        for car in list(bridge):
            car[1] += 1
            if car[1] == bridge_length:
                now_weight -= car[0]
                bridge.popleft()

    answer += bridge_length
    return answer