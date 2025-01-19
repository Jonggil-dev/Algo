import java.util.*;

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        HashMap<Integer, Integer> older = new HashMap<>();
        HashMap<Integer, Integer> younger = new HashMap<>();
        
        
        for(int top :topping){
            int check = older.getOrDefault(top, 0);
            older.put(top, check + 1);
        }
        
         for(int top :topping){
            int yCheck = younger.getOrDefault(top, 0);
            younger.put(top, yCheck + 1);
            
            Integer oCheck = older.get(top);
             
            if(oCheck == null || oCheck == 1){
                older.remove(top);
            } else {
                older.put(top, oCheck - 1);
            }
            
            if(older.size() == younger.size()){
                answer += 1;
            }
        }

        return answer;
    }
}