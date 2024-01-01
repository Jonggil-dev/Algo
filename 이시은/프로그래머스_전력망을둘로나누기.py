# 프로그래머스 전력망 둘로 나누기

# 트리 구조, 완전탐색

def solution(n, wires):
    def BFS(start, wire):
        queue = [start]
        visited = [False] * 101
        visited[start] = True

        while queue:
            now = queue.pop(0)
            for next in adj_list[now]:
                if [now, next] == wire or [next, now] == wire or visited[next]:
                    continue

                queue.append(next)
                visited[next] = True

        return sum(visited)

    adj_list = [[] for _ in range(n+1)]
    for wire in wires:
        # 양방향 연결
        adj_list[wire[0]].append(wire[1])
        adj_list[wire[1]].append(wire[0])

    diff = 100
    for wire in wires:
        A_len = BFS(wire[0], wire)
        B_len = BFS(wire[1], wire)
        # print(A_len, B_len)
        if abs(A_len - B_len) < diff:
            diff = abs(A_len - B_len)

    answer = diff
    return answer


n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

n = 4
wires = [[1,2],[2,3],[3,4]]

n = 7
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

print(solution(n, wires))