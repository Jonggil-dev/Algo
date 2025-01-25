def solution(triangle):
    r, c = len(triangle), len(triangle[-1])
    dp = [[0] * c for _ in range(r)]
    dp[0][0] = triangle[0][0]
    answer = 0
    
    for i in range(1, r):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
                
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                
            else:
                dp[i][j] = max(triangle[i][j], dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
            
            answer = max(answer, dp[i][j])
                
    return answer