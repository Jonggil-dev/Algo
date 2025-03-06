def solution(triangle):
    answer = 0
    N=len(triangle)
    res=[[0]*i for i in range(1,N+1)]
    res[0][0]=triangle[0][0]
    for i in range(N-1):
        for j in range(i+1):
            print(triangle[i+1],i,j)
            res[i+1][j]=max(res[i+1][j],triangle[i+1][j]+res[i][j])
            res[i+1][j+1]=max(res[i+1][j+1],triangle[i+1][j+1]+res[i][j])
    answer=max(res[N-1])
    for i in range(N):
        print(res[i])
    return answer


triangle=eval(input())
print(solution(triangle))
