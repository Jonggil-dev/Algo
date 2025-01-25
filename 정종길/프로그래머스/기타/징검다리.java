import java.util.*;
import java.util.stream.Collectors; 

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        int start = 0;
        int end = distance;
        int delete, prevRock;
        
        List<Integer> wrRocks = Arrays.stream(rocks)
            .boxed()
            .collect(Collectors.toList());

        Collections.sort(wrRocks);
        wrRocks.add(distance);

        while(start <= end){
            
            int mid = (start + end) / 2;
            delete = 0;
            prevRock = 0;
            
            for(int rock : wrRocks){
                if((rock - prevRock) < mid){
                    delete += 1;
                }else{
                    prevRock = rock;
                }
                
                if(delete > n){
                    break;
                }
            }
            
            if (delete > n){
                end = mid - 1;
                
            } else {
                start = mid + 1;
                answer = mid;
                
            }
        }

        return answer;
    }
}