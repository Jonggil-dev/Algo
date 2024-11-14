'''
1. dfs로 하위부터 올라오면서 dp 테이블 갱신 
2. dp 테이블 = [본인이 선택 되지 않은 경우 최소 값, 본인이 선택된 경우 최소 값] 
3. 위 2가지 작업을 통해 각 그룹별 팀장은 하위 그룹을 포함 해서 [본인이 선택 되지 않았을 때, 본인이 선택 되었을 때 ]이 최소 값이 기록
4. 추가로 본인이 선택 되지 않았을 때는 -> 팀원 모두가 선택되지 않은 값이 반영 될 수 있으므로 un_cnt와 min_diff를 따로 관리해서 처리
'''

def solution(sales, links):
    global graph, dp

    graph = [[] for _ in range(len(sales) + 1)]
    dp = [[0, 0] for _ in range(len(sales) + 1)]
    
    for s, e in links:
        graph[s].append(e)
        
    search(1, sales)
    
    return min(dp[1][0], dp[1][1])

def search(leader, sales):
    global graph, dp
    
    if not graph[leader]:
        dp[leader][1] = sales[leader - 1]
        return
    
    uc_cnt = 0
    min_diff = 1e9
    
    for member in graph[leader]:
        search(member, sales)
        
        if dp[member][0] < dp[member][1]:
            uc_cnt += 1
            min_diff = min(min_diff, dp[member][1] - dp[member][0])

        dp[leader][0] += min(dp[member][0], dp[member][1])        
        dp[leader][1] += min(dp[member][0], dp[member][1])
        
    dp[leader][1] += sales[leader - 1]
    if uc_cnt == len(graph[leader]):
        dp[leader][0] += min_diff
 