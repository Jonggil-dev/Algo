'''
1. dsf로 리프에서 올라오면서 dp[본인] = [2 - (1), 2- (2)] 사용 
2. 리프에서 올라오며 각 노드에 대해서 2가지의 경우로 나누어 생각하면 됨
(1) 본인이 선택이 되지 않았을 자녀를 루트로 하는 각 서브 트리들의 최솟 값
 -> 각 서브 트리들의 최솟 값의 합을 하면 되는데
 -> 하지만, 이 경우 본인 + 자녀가 모두 선택이 되지 않는 경우가 발생 할 수 있음
 -> 이 경우를 처리하기 위해 min_diff로 보정 값을 관리하며 cnt로 해당 경우가 되는지 확인을 하고, 만약 해당이 된다면 min_diff 보정 값을 더해주기
 
(2) 본인이 선택이 됐을 경우 자녀를 루트로 하는 각 서브 트리들의 최솟 값
 -> 각 서브 트리들의 최솟 값의 합 + 본인의 값을 하면
 -> 본인이 선택이 됐을 경우에 본인을 루트로 하는 서브트리의 최솟 값이 됨
'''

def solution(sales, links):
    n = len(sales)
    dp = [[0,0] for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    
    for p, s in links:
        graph[p].append(s)
        
    dfs(1, dp, sales, graph)
    
    return min(dp[1])

def dfs(now, dp, sales, graph):
    
    if not graph[now]:
        dp[now][1] = sales[now - 1]
        return
    
    cnt, min_diff = 0, 1e9
    for son in graph[now]:
        dfs(son, dp, sales, graph)
        
        if dp[son][0] < dp[son][1]:
            cnt += 1
            min_diff = min(min_diff, dp[son][1] - dp[son][0])
            
        dp[now][0] += min(dp[son][0], dp[son][1])
        dp[now][1] += min(dp[son][0], dp[son][1])
        
    dp[now][1] += sales[now - 1]
    if cnt == len(graph[now]):
        dp[now][0] += min_diff
        