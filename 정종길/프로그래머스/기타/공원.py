def solution(mats, park):
    answer = 0
    mats.sort(reverse = True)
    
    for mat in mats:
        for i in range(len(park)):
            for j in range(len(park[0])):
                if park[i][j] == "-1":
                    if check(i, j, mat, park):
                        return mat
    return -1

def check(i, j, mat, park):
    for k in range(mat):
        for l in range(mat):
            if i + k >= len(park) or j + l >= len(park[0]) or park[i + k][j + l] != "-1":
                return False
    return True

