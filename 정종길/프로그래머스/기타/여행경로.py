## 재귀 dfs 실행 전에, 현재 방문된 노드는 제외 하여 처리해야 됨
## 다음 dfs 실행 함수에서 현재 방문된 노드를 pop 해서 방문 리스트를 던져주고,
## dfs가 끝나면 insert를 이용해서 리스트 내 원래 위치에 다시 가져다 두기
## append가 아니라 insert를 쓰는거는 가능한 경로가 여러개 일 때 알파벳 순으로 처리하기 위함 임
## 처음 airports를 sort했기 때문에 첫 번 째로 종료 조건을 만나면 그냥 dfs 전체 종료 시켜버리면 됨

import copy


def solution(tickets):
    global answer, N
    N = len(tickets)

    answer = []
    airports = {}

    for start, end in tickets:
        airports[start] = airports.get(start, []) + [end]

    for airport in airports.values():
        airport.sort()

    dfs("ICN", airports, ["ICN"])

    return answer


def dfs(now, airports, visited):
    global answer, N

    if len(visited) == (N + 1):
        answer = visited
        return True

    if airports.get(now):
        copied = copy.deepcopy(airports[now])
        for i in range(len(copied)):
            airport = airports[now].pop(i)
            if dfs(airport, airports, visited + [airport]):
                return True
            airports[now].insert(i, airport)
