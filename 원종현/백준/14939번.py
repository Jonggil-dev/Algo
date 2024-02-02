def ccw(ax, ay, bx, by, cx, cy):
    """ 벡터의 외적을 계산하는 함수 """
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)

def check_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    """ 선분 교차 여부를 판단하는 함수 """
    ab = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    cd = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

    if ab == 0 and cd == 0:
        if (min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and
                min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2)):
            return True
        return False

    return ab <= 0 and cd <= 0

# 입력 예시: x1, y1, x2, y2, x3, y3, x4, y4
x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())

print('01'[check_intersection(x1,y1,x2,y2,x3,y3,x4,y4)])
