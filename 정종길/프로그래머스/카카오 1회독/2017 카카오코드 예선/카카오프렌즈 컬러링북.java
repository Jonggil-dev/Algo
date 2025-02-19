import java.util.*;

class Solution {
    
    int[][] visited;
    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};
    
    public int[] solution(int m, int n, int[][] picture) {
        int[] answer = new int[2];
        visited = new int[m][n];
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(picture[i][j] != 0 && visited[i][j] == 0){
                    int width = bfs(i, j, picture, m, n);
                    answer[0] += 1;
                    answer[1] = Math.max(answer[1], width);
                }
            }
        }

        return answer;
    }
    
    public int bfs(int si, int sj, int[][] picture, int m, int n){
        
        Deque<Integer[]> q = new LinkedList<>();
        
        visited[si][sj] = 1;
        int area = picture[si][sj];
        int cnt = 1;
        q.add(new Integer[] {si, sj});
            
        while(!q.isEmpty()){
            Integer[] li = q.pollFirst();
            int i = li[0];
            int j = li[1];
            
            for(int d = 0; d < 4; d++){
                int ni = i + dx[d];
                int nj = j + dy[d];
                if(0 <= ni && ni < m && 0 <= nj && nj < n){
                    if(area == picture[ni][nj] && visited[ni][nj] == 0){
                        cnt += 1;
                        visited[ni][nj] = 1;
                        q.add(new Integer[] {ni, nj});
                    }
                }
            }
        }
        return cnt;
    }
}