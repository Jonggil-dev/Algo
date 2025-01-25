def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        l1 = []
        for j in range(len(arr2[0])):
            a = 0
            for k in range(len(arr2)):
                a += arr1[i][k] * arr2[k][j]
            l1.append(a)
        answer.append(l1)

    return answer