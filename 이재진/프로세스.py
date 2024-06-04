from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    process = deque([chr(i) for i in range(65,65+len(priorities))])
    location = chr(location+65)
    max_num = max(priorities)
    cnt = 1
    while True:
        tmp = priorities.popleft()
        if tmp < max_num:
            priorities.append(tmp)
            process.append(process.popleft())
        elif tmp == max_num:
            if location == process.popleft():
                return cnt
            else:
                max_num = max(priorities)
                cnt += 1
    print(process)
    return answer
