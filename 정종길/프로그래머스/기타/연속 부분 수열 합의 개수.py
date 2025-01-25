def solution(elements):
    data = set()
    extends = elements * 2
    
    for i, _ in enumerate(elements):
        tot = 0
        for num in extends[i : i + len(elements)]:
            tot += num
            data.add(tot)
            
    return len(data)