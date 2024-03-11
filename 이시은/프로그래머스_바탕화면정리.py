# 프로그래머스 Lv1 바탕화면 정리


def solution(wallpaper):
    row_tmp = []
    for row in range(len(wallpaper)):
        if '#' in wallpaper[row]:
            row_tmp.append(row)
    col_tmp = []
    rotated = list(zip(*wallpaper))
    for col in range(len(wallpaper[0])):
        if '#' in rotated[col]:
            col_tmp.append(col)

    return [row_tmp[0], col_tmp[0], row_tmp[-1]+1, col_tmp[-1]+1]

wallpaper = [".#...", "..#..", "...#."]
wallpaper = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
wallpaper = ["..", "#."]

print(solution(wallpaper))