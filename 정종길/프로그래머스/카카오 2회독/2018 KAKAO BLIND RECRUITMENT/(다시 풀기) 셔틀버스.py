def solution(n, t, m, timetable):
    orders = []
    answer = 0
    
    for time in timetable:
        orders.append(time_to_min(time))
    
    orders.sort()    
    
    idx = cnt = lst = 0
    bus = 9 * 60
    
    while n > 0:
        n -= 1  
        cnt = 0 

        while idx < len(orders) and orders[idx] <= bus and cnt < m:
            cnt += 1
            idx += 1

        if n == 0:
            if cnt < m:
                answer = bus
            else:
                answer = orders[idx - 1] - 1
        bus += t

    return f'{(answer)//60:02d}:{(answer) % 60:02d}'


def time_to_min(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)