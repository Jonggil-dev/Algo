from collections import deque
def solution(msg):
    answer = []
    msg = deque(msg)
    dic = dict()
    for i in range(1, 27):
        dic[chr(64 + i)] = i
    num = 27
    n = len(msg)
    flag = 0
    while msg:
        cnt = 0
        tmp = ""
        while True:
            if cnt >= n:
                flag = 1
                answer.append(dic[tmp])
                break
            elif tmp+msg[cnt] in dic:
                tmp += msg[cnt]
                cnt += 1
            else:
                answer.append(dic[tmp])
                tmp += msg[cnt]
                dic[tmp] = num
                num += 1
                n -= cnt
                for _ in range(cnt):
                    msg.popleft()
                break
        if flag:
            break
    return answer
