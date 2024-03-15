import heapq


def solution(operations):
    min_heapq = []
    answer = []
    flag = True

    for nums in operations:
        operator, num = nums.split()

        if operator == "I":
            heapq.heappush(min_heapq, (int(num), -int(num)))

        elif operator == "D":
            if min_heapq:
                if num == "-1":
                    heapq.heappop(min_heapq)
                    flag = True

                else:
                    min_heapq.sort(key=lambda x: x[1], reverse=True)
                    min_heapq.pop()

                    if flag:
                        flag = False
                        heapq.heapify(min_heapq)

    if min_heapq:
        min_heapq.sort(key=lambda x: x[1], reverse=True)
        print(min_heapq)
        answer.append(-min_heapq.pop()[1])
        heapq.heapify(min_heapq)
        answer.append(heapq.heappop(min_heapq)[0])

    else:
        answer = [0, 0]

    return answer