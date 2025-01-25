def solution(n, wires):
    def dfs(i):
        visited[i] = 1
        for node in Arr[i]:
            if not visited[node]:
                dfs(node)

    Arr = [[] for _ in range(n + 1)]
    answer = 100

    for wire in wires:
        Arr[wire[0]].append(wire[1])
        Arr[wire[1]].append(wire[0])

    for i in range(n + 1):

        check_li = [0] * (n + 1)

        while Arr[i]:

            tmp = Arr[i].pop(0)
            Arr[tmp].remove(i)

            if check_li[tmp]:
                Arr[i].append(tmp)
                Arr[tmp].append(i)
                break

            check_li[tmp] = 1

            visited = [0] * (n + 1)
            dfs(i)

            answer = min(abs(n - visited.count(1) - visited.count(1)), answer)

            Arr[i].append(tmp)
            Arr[tmp].append(i)

    return answer
