def val(place):
    d1 = [[0,1],  [1,0],  [0,-1],  [-1,0]]
    d2 = [[1,1], [1,-1], [-1,-1], [-1,1]]
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                for d in d1:
                    ni, nj = i+d[0], j+d[1]
                    if 0<=ni<5 and 0<=nj<5 and place[ni][nj] == "P":
                        return 0
                for d in d1:
                    ni, nj = i+(d[0]*2), j+(d[1]*2)
                    if 0<=ni<5 and 0<=nj<5 and place[ni][nj] == "P":
                        if place[(i+ni)//2][(j+nj)//2] != "X":
                            return 0
                for d in d2:
                    ni, nj = i+d[0], j+d[1]
                    if 0<=ni<5 and 0<=nj<5 and place[ni][nj] == "P":
                        if place[i][nj] != "X" or place[ni][j] != "X":
                            return 0  
    return 1

def solution(places):
    answer = []
    for place in places:
        if val(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer