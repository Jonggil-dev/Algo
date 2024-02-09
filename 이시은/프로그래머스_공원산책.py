# 프로그래머스 lv1 공원산책
# 이 문제를 이렇게 어렵게 푸는게 맞나;; 정신차리면 다시 풀어보자..

def solution(park, routes):
    def find_S(maxR, maxC):
      # 시작 지점 찾기
      for r in range(maxR):
        for c in range(maxC):
          if park[r][c] == "S":
            return [r, c]
          
    maxR = len(park)
    maxC = len(park[0])
    point = find_S(maxR, maxC)

    for route in routes:
        op, n = route.split()
        if op == "E":
          tmp_col = point[1]
          for _ in range(int(n)):
              tmp_col += 1
              if (tmp_col < 0 or tmp_col >= maxC) or park[point[0]][tmp_col] == "X":
                break
          else:
            point = [point[0], tmp_col]
        if op == "W":
          tmp_col = point[1]
          for _ in range(int(n)):
              tmp_col -= 1
              if (tmp_col < 0 or tmp_col >= maxC) or park[point[0]][tmp_col] == "X":
                break
          else:
            point = [point[0], tmp_col]
        if op == "N":
          tmp_row = point[0]
          for _ in range(int(n)):
              tmp_row -= 1
              if (tmp_row < 0 or tmp_row >= maxR) or park[tmp_row][point[1]] == "X":
                break
          else:
            point = [tmp_row, point[1]]
        if op == "S":
          tmp_row = point[0]
          for _ in range(int(n)):
              tmp_row += 1
              if (tmp_row < 0 or tmp_row >= maxR) or park[tmp_row][point[1]] == "X":
                break
          else:
            point = [tmp_row, point[1]]
        
    answer = point
    return answer

park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]
print(solution(park, routes))
park = ["SOO","OXX","OOO"]
routes = ["E 2","S 2","W 1"]
print(solution(park, routes))
park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]
print(solution(park, routes))
