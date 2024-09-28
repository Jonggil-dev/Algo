def solution(lines):
    lines_toSec = []
    for line in lines:
        lines_toSec.append(toSec(line))

    answer = 0
    for i in range(len(lines_toSec)):
        for time_point in [lines_toSec[i][0], lines_toSec[i][1]]:
            window_start = time_point
            window_end = window_start + 1000
            count = 0
            for s, e in lines_toSec:
                if s < window_end and e >= window_start:
                    count += 1
            answer = max(answer, count)
    return answer

def toSec(string):
    _, time, period = string.split()
    time_parts = time.split(':')
    hours = int(time_parts[0]) * 3600 * 1000
    minutes = int(time_parts[1]) * 60 * 1000
    seconds_and_millis = time_parts[2].split('.')
    seconds = int(seconds_and_millis[0]) * 1000
    millis = int(seconds_and_millis[1]) if len(seconds_and_millis) > 1 else 0
    end_time = hours + minutes + seconds + millis

    processing_time = float(period[:-1]) * 1000
    start_time = end_time - processing_time + 1

    return (start_time, end_time)
