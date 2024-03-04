package 원종현.SWEA;

import java.io.*;
import java.util.*;

// SWEA
class Solution {
    static String[][] li;
    static int[][] minemap; // 지뢰 맵을 int로 변경하여 관리
    static boolean[][] visited; // 방문 여부를 확인하기 위한 배열
    static int N;
    static int res;

    static class Tuple {
        public int x;
        public int y;

        public Tuple(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int tc = Integer.parseInt(br.readLine());
        for (int sc = 1; sc <= tc; sc++) {
            N = Integer.parseInt(br.readLine());
            li = new String[N][N];
            minemap = new int[N][N];
            visited = new boolean[N][N];
            res = 0;
            for (int i = 0; i < N; i++) {
                String[] tmp = br.readLine().split("");
                for (int j = 0; j < N; j++) {
                    li[i][j] = tmp[j];
                    if (li[i][j].equals("*")) minemap[i][j] = -1; // 지뢰는 -1로 표시
                }
            }
            fillminemap();
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (!visited[i][j] && minemap[i][j] == 0) {
                        res++; // 빈 칸 중에서 지뢰가 없는 칸을 클릭
                        cleanclick(i, j); // 주변 칸을 자동으로 연다
                    }
                }
            }
            // 지뢰가 없는 칸이지만 단독으로 클릭해야 하는 칸 계산
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (!visited[i][j] && minemap[i][j] > 0) {
                        res++;
                    }
                }
            }
            bw.write("#" + sc + " " + res + "\n");
        }

        bw.flush();
    }

    static void fillminemap() {
        for (int x = 0; x < N; x++) {
            for (int y = 0; y < N; y++) {
                if (li[x][y].equals(".")) {
                    int mines = getmines(x, y);
                    minemap[x][y] = mines;
                }
            }
        }
    }

    static int getmines(int x, int y) {
        int tmp = 0;
        for (int dx = -1; dx <= 1; dx++) {
            for (int dy = -1; dy <= 1; dy++) {
                if (dx == 0 && dy == 0) continue; // 자기 자신은 제외
                int nx = x + dx;
                int ny = y + dy;
                if (nx >= 0 && nx < N && ny >= 0 && ny < N && li[nx][ny].equals("*")) {
                    tmp++;
                }
            }
        }
        return tmp;
    }

    static void cleanclick(int x, int y) {
        if (x < 0 || x >= N || y < 0 || y >= N || visited[x][y] || minemap[x][y] == -1) return;
        visited[x][y] = true; // 방문 표시
        if (minemap[x][y] > 0) return; // 지뢰 주변 숫자가 있는 경우 더 이상 확장하지 않음

        for (int dx = -1; dx <= 1; dx++) {
            for (int dy = -1; dy <= 1; dy++) {
                cleanclick(x + dx, y + dy);
            }
        }
    }
}
