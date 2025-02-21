import java.util.*;
class Solution {
    int answer = 0;
    
    public int solution(int n) {
        dfs(n - 2, 2);
        return answer;
    }
    
    private void dfs(int num, int plsCnt) {
        
        if(num == 3 && plsCnt == 2){
            answer += 1;
            return;
        }
        
        if(num < 3 || 2 * ((Math.log(num) / Math.log(3))) < plsCnt){
            return;
        }
    
        if(num % 3 == 0 && plsCnt >= 2){
            dfs((int) (num / 3), plsCnt - 2);
        }
        
        dfs(num - 1, plsCnt + 1);
    }
    
}