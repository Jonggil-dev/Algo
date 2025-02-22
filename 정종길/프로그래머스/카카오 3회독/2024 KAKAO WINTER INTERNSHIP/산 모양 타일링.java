import java.util.*;

class Solution {
    public int solution(int n, int[] tops) {
        
        int[] an = new int[n];
        int[] bn = new int[n];
        
        if (tops[0] == 1){
            an[0] = 4;
            bn[0] = 3;
        }else{
            an[0] = 3;
            bn[0] = 2;
        }
        
        for(int i = 1; i < n; i++){
            if(tops[i] == 1){
                an[i] = 3 * an[i - 1] + bn[i - 1];
                bn[i] = 2 * an[i - 1] + bn[i - 1];
            }else{
                an[i] = 2 * an[i - 1] + bn[i - 1];
                bn[i] = an[i - 1] + bn[i - 1];
            }
            an[i] %= 10007;
            bn[i] %= 10007;
        }
        return an[n-1];
    }
}