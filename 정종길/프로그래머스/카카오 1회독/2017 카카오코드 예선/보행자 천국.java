import java.util.*;
class Solution {
    int MOD = 20170805;
    public int solution(int m, int n, int[][] cityMap) {
        int answer = 0;
        int[][][] map = new int[m][n][2];
        
        for(int j = 1; j < n; j++){
            if(cityMap[0][j] == 1){
                break;
            }else{
                map[0][j][0] = 1;
            }
        }
        
        for(int i = 1; i < m; i++){
            if(cityMap[i][0] == 1){
                break;
            }else{
                map[i][0][1] = 1;
            }
        }
        
        for(int row = 1; row < m; row++){
            for(int col = 1; col < n; col++){
                if(cityMap[row][col] == 1){
                    continue;
                    
                }else {
                    if (cityMap[row - 1][col] == 2){
                        map[row][col][1] += map[row - 1][col][1];
                    } else{
                        map[row][col][1] += map[row - 1][col][0] + map[row - 1][col][1];
                    }
                    
                    if (cityMap[row][col - 1] == 2){
                        map[row][col][0] += map[row][col - 1][0];
                    } else{
                        map[row][col][0] += map[row][col - 1][0] + map[row][col - 1][1];
                    }
                    map[row][col][0] %= 20170805;
                    map[row][col][1] %= 20170805;
                }
            }
        }
        
        return (map[m-1][n-1][0] + map[m-1][n-1][1]) % 20170805;
    }
}