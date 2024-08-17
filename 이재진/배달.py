import heapq
def solution(N, road, K):
    answer = 0
    dic = {i:[] for i in range(1, N+1)}
    for a,b,c in road:
        dic[a].append([b,c])
        dic[b].append([a,c])
    
    def dijkstra():
        pq = []
        heapq.heappush(pq, (0,1))
        distance[1] = 0
        while pq:
            dis, cur = heapq.heappop(pq)
            if distance[cur] >= dis:
                for n, weight in dic[cur]:
                    new_weight = distance[cur] + weight
                    if distance[n] >= new_weight:
                        distance[n] = new_weight
                        heapq.heappush(pq, (new_weight, n))
            
        
        
    distance = [float("inf")] * (N+1)
    dijkstra()
    for i in distance:
        if i <= K:
            answer += 1
    return answer
