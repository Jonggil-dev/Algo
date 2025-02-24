import java.util.*;

class Solution {
    int ccoin;
    
    public int solution(int coin, int[] cards) {
        int answer = 0;
        ccoin = coin;
        
        int n = cards.length;
        
        HashSet<Integer> havings = new HashSet<>();
        HashSet<Integer> candidates = new HashSet<>();
        
        for(int i = 0 ; i < n / 3; i++){
            havings.add(cards[i]);
        }

        int j = n / 3;
        
        while(j < n){
            answer += 1;
            for(int k = 0 ; k < 2; k++){
                candidates.add(cards[j]);
                j += 1;
            }
            
            if(!check_sum(havings, candidates, n)){
                return answer;
            }
        }
        
        answer += 1;
        
        return answer;
    }
    
    private Boolean check_sum(HashSet<Integer> havings, HashSet<Integer> candidates, int n){

        for(Integer h : havings){
            if(havings.contains(n + 1 - h)){
                havings.remove(h);
                havings.remove(n + 1 - h);
                return true;
            }
        }
        
        if(ccoin < 1){
            return false;
        }
        
        for(Integer h : havings){
            if(candidates.contains(n + 1 - h)){
                havings.remove(h);
                candidates.remove(n + 1 - h);
                ccoin -= 1;
                return true;
            }
        }
        
        if(ccoin < 2){
            return false;
        }
        
        for(Integer c : candidates){
            if(candidates.contains(n + 1 - c)){
                candidates.remove(c);
                candidates.remove(n + 1 - c);
                ccoin -= 2;
                return true;
            }
        }
        
        return false;
    }
}