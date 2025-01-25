def solution(arr):
    test = arr[-1]
    for i in range(1, 1000000000):
        flag = True
        answer = test * i
        for j in range(len(arr)):
            if answer < arr[j] or answer % arr[j] != 0:
                flag = False
                break
        if flag == True:
            return answer