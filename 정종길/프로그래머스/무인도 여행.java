import java.util.*;

class Solution {
    static boolean[][] visited ;
    static int row;
    static int col;

    public List<Integer> solution(String[] maps) {
        List<Integer> answer = new ArrayList<>();
        row = maps.length;
        col = maps[0].length();
        visited = new boolean[row][col];

        for(int i = 0; i < row; i ++ ){
            for(int j = 0; j < col; j ++){
                if (maps[i].charAt(j) != 'X' && visited[i][j] == false){
                    int distance = bfs(maps[i].charAt(j), i, j, maps);
                    answer.add(distance);
                }
            }
        }

        if(answer.isEmpty()){
            answer.add(-1);
        } else {
            Collections.sort(answer);
        }
        return answer;
    }

    public int bfs(char num, int i, int j, String[] maps){
        Queue<Integer[]> queue = new LinkedList<>();
        int area = 0;
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        queue.add(new Integer[]{Integer.parseInt(String.valueOf(num)), i, j});

        visited[i][j] = true;

        while(!queue.isEmpty()){
            Integer[] arr = queue.poll();
            area += arr[0];
            int x = arr[1];
            int y = arr[2];

            for(int k = 0; k < 4; k ++){
                int nx = x + dx[k];
                int ny = y + dy[k];
                if(0 <= nx && nx < row && 0 <= ny && ny < col){
                    if(visited[nx][ny] == false && maps[nx].charAt(ny) != 'X'){
                        visited[nx][ny] = true;
                        queue.add(new Integer[] { Integer.parseInt(String.valueOf(maps[nx].charAt(ny))), nx, ny });
                    }
                }
            }

        }
        return area;
    }

}