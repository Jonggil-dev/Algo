from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 1
    now = 0
    now_weight = 0
    bridge = deque()
    while True:
        while bridge and bridge[0][1] >= bridge_length:
            tmp = bridge.popleft()
            now_weight -= truck_weights[tmp[0]]

        if now < len(truck_weights) and len(bridge) <= bridge_length and truck_weights[now] + now_weight <= weight:
            bridge.append([now, 0])
            now_weight += truck_weights[now]
            now += 1
        for i in range(len(bridge)):
            bridge[i][1] += 1

        if now_weight == 0 and now == len(truck_weights):
            break
        time += 1
    return time
