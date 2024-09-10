import java.util.*;

class Solution {
    public int solution(int[] stones, int k) {
        int start = 1;
        int end = Arrays.stream(stones).max().getAsInt();
        
        while(start < end){
            int mid = (start + end) / 2;
            int cnt = 0;
            
            for(int stone : stones){
                if((stone - mid) <= 0){
                    cnt += 1;
                }else{
                    cnt = 0;
                }
                
                if(cnt >= k){
                    break;
                }
            }
            
            if(cnt >= k){
                end = mid;
            }else{
                start = mid + 1;
            }
            
        }
        
        return start;
    }
}