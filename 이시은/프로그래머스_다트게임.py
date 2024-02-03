# 프로그래머스 [1차]다트 게임
def solution(dartResult):
    bonus_dict = {'S': 1, 'D': 2, 'T': 3}
    answer = 0
    points = []
    tmp = dartResult[0]
    for s in dartResult[1:]:
        if s.isdigit() and not tmp.isdigit():
            points.append(tmp)
            tmp = s
        else:
            tmp += s
    points.append(tmp)

    n_points = [0] * len(points)
    for i, point in enumerate(points):
        if not point[1].isdigit():
            num = int(point[0]) ** (bonus_dict[point[1]])
        else:
            num = 10 ** (bonus_dict[point[2]])

        if point[-1] in ['*', '#']:
            option = point[-1]
            if option == '*':
                if i == 0:
                    n_points[0] = num * 2
                n_points[i-1] *= 2
                num *= 2
            if option == '#':
                num *= (-1)
        n_points[i] = num

    return sum(n_points)

dartResult = "1S2D*3T"
dartResult = "1D2S#10S"
dartResult = "1D2S0T"
dartResult = "1S*2T*3S"
dartResult = "1D#2S*3S"
dartResult = "1T2D3D#"
dartResult = "1D2S3T*"

print(solution(dartResult))