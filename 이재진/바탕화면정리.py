def solution(wallpaper):
    ls = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                ls.append((i,j))
    left_i = 100
    left_j = 100
    right_i = 0
    right_j = 0
    for i in ls:
        if left_i > i[0]:
            left_i = i[0]
        if right_i < i[0]:
            right_i = i[0]
        if left_j > i[1]:
            left_j = i[1]
        if right_j < i[1]:
            right_j = i[1]
    answer = [left_i, left_j, right_i+1, right_j+1]
    
    print(ls)
    return answer
