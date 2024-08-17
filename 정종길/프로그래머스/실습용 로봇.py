def solution(command):
    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direct = 1
    x = y = 0
    
    for com in command:
        if com == "R":
            direct = (direct + 1) % 4
        elif com == "L":
            direct = (direct - 1) % 4
        elif com == "G":
            x, y = x + deltas[direct][0], y + deltas[direct][1]
        else:
            x, y = x - deltas[direct][0], y - deltas[direct][1]
    
    answer = [x, y]
    return answer