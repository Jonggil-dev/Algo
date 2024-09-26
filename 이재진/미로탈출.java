import java.util.*;

class Solution {
    
    public int[][] make_dis(String[] maps) {
        int[][] dis = new int[maps.length][maps[0].length()];
        for (int i=0;i<maps.length;i++){
            for (int j=0;j<maps[0].length();j++) {
                dis[i][j] = 9999999;
            }
        }
        return dis;
    }
    
    public int algo(String[] maps, int si, int sj, int ei, int ej) {
        int[][] dij = {{0,1}, {1,0}, {0,-1}, {-1,0}};
        int[][] dis = make_dis(maps);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        int[] first = {0,si,sj,0};
        pq.offer(first);
        while(!pq.isEmpty()) {
            int[] now = pq.poll();
            int w = now[0];
            int ci = now[1];
            int cj = now[2];
            int ans = now[3];
            if (ci == ei && cj == ej) {
                return ans;
            }
            if (w <= dis[ci][cj]) {
                for (int[] d:dij) {
                    int ni = ci+d[0];
                    int nj = cj+d[1];
                    if (0<=ni && ni<maps.length && 0<=nj && nj<maps[0].length() && maps[ni].charAt(nj) != 'X') {
                        if (dis[ni][nj] > w+1) {
                            dis[ni][nj] = w+1;
                            int[] next = {w+1, ni, nj, ans+1};
                            pq.offer(next);
                        }
                    }
                }
            }
        }
        return -1;
    }
    
    public int solution(String[] maps) {
        int answer = 0;
        int si = 0;
        int sj = 0;
        int ei = 0;
        int ej = 0;
        int li = 0;
        int lj = 0;
        
        for (int i=0;i<maps.length;i++) {
            for (int j=0;j<maps[i].length();j++) {
                if (maps[i].charAt(j) == 'S') {
                    si = i;
                    sj = j;
                } else if (maps[i].charAt(j) == 'E') {
                    ei = i;
                    ej = j;
                } else if (maps[i].charAt(j) == 'L') {
                    li = i;
                    lj = j;
                }
            }
        }
        if (algo(maps,si,sj,li,lj) == -1 || algo(maps,li,lj,ei,ej) == -1) {
            return -1;
        }
        
        answer += algo(maps,si,sj,li,lj);
        System.out.println(answer);
        answer += algo(maps,li,lj,ei,ej);
        return answer;
    }
}
