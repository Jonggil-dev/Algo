def solution(alp, cop, problems):
    answer = 0
    max_alp_req, max_cop_req = (0, 0)

    for problem in problems:
        max_alp_req = max(max_alp_req, problem[0])
        max_cop_req = max(max_cop_req, problem[1])

    max_alp_req = max(alp, max_alp_req)
    max_cop_req = max(cop, max_cop_req)

    dp = [[1e9] * (max_cop_req + 1) for _ in range(max_alp_req + 1)]

    dp[alp][cop] = 0

    for i in range(alp, max_alp_req + 1):
        for j in range(cop, max_cop_req + 1):
            if i < max_alp_req:
                dp[i + 1][j] = min(dp[i][j] + 1, dp[i + 1][j])

            if j < max_cop_req:
                dp[i][j + 1] = min(dp[i][j] + 1, dp[i][j + 1])

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i + alp_rwd, max_alp_req)
                    new_cop = min(j + cop_rwd, max_cop_req)
                    dp[new_alp][new_cop] = min(dp[i][j] + cost, dp[new_alp][new_cop])

    return dp[max_alp_req][max_cop_req]