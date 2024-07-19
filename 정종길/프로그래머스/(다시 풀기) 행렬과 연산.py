from collections import deque


def solution(rc, operations):
    body = deque()
    edge = [deque(), deque()]

    for row in rc:
        body.append(deque(row[1:-1]))
        edge[0].append(row[0])
        edge[1].append(row[-1])

    for operation in operations:
        if operation[0] == "S":
            body.appendleft(body.pop())
            edge[0].appendleft(edge[0].pop())
            edge[1].appendleft(edge[1].pop())

        else:
            body[0].appendleft(edge[0].popleft())
            edge[1].appendleft(body[0].pop())
            body[-1].append(edge[1].pop())
            edge[0].append(body[-1].popleft())

    answer = []
    for i in range(len(rc)):
        answer.append([edge[0][i]] + list(body[i]) + [edge[1][i]])

    return answer
