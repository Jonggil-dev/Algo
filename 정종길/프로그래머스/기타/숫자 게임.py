def solution(A, B):
    answer = 0
    
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    point_b = 0

    for num in A:
        if point_b >= len(B):
            break
            
        if num < B[point_b]:
            point_b += 1
            answer += 1
        
    return answer