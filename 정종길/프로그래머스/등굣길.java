import java.util.*;

class Solution {
    public long solution(int m, int n, int[][] puddles) {
        long[][] arr = new long[n][m];

        arr[0][0] = 1;
        
        for(int i = 0; i < n; i ++){
            for(int j = 0; j < m; j++){
                if(check(puddles, i, j)){
                    arr[i][j] = 0;
                    continue;
                }
                    
                if(i == 0){
                    if(j - 1 >= 0){
                        arr[i][j] = arr[i][j -1];
                    }
                }else if(j == 0){
                    if(i - 1 >= 0){
                        arr[i][j] = arr[i-1][j];
                    }
                }else{
                    arr[i][j] = arr[i - 1][j] + arr[i][j -1];
                }  
                arr[i][j] %= 1000000007;
            }
        }
        return arr[n - 1][m - 1] % 1000000007;
    }
    
    boolean check(int[][] puddles, int i, int j){
         for(int[] puddle: puddles){
             if(i == (puddle[1] - 1)){
                if(j == (puddle[0] - 1)){
                    return true;
                }
            }
        }
        return false;
    }
    
}