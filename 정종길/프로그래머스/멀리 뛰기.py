def solution(n):
    if n  == 1:
        return 1
    else:
        Arr = [0] * n
        Arr[0] = 1
        Arr[1] = 2
        for i in range(2,n):
            Arr[i] = Arr[i-1] + Arr[i-2]
        return Arr[-1] %1234567