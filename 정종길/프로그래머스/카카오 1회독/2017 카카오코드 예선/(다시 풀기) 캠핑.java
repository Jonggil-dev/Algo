import java.util.*;

class Solution {
    public int solution(int n, int[][] data) {
        int answer = 0;
        Arrays.sort(data, ((a, b) -> {if(a[0] != b[0]){return a[0] - b[0];}return a[1] - b[1];}));
        
        for(int i = 0; i < n - 1; i++){
            int x = data[i][0];
            int y = data[i][1];
            int lower_y = 0;
            int upper_y = Integer.MAX_VALUE;
            int tmpLy = 0;
            int tmpUy = Integer.MAX_VALUE;

            for(int j = i + 1; j < n; j++){
                int nx = data[j][0];
                int ny = data[j][1];
                
                if (j > i + 1 && data[j - 1][0] != data[j][0]){
                    upper_y = tmpUy;
                    lower_y = tmpLy;
                }
                
                if (x == nx || y == ny){
                    continue;
                }
                
                if (ny > y) {
                    if(ny <= upper_y){
                        answer += 1;
                    }
                    tmpUy = Math.min(tmpUy, ny);
                }else{
                    if(lower_y <= ny){
                        answer += 1;
                    }
                    tmpLy = Math.max(tmpLy, ny);
                }
            }
        }
        
        return answer;
    }
}