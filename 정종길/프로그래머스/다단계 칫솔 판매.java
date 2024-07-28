import java.util.*;

class Solution {
    static int[] answer;
    static Map<String, Integer> idxMap;

    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {

        answer = new int[enroll.length];
        idxMap = new HashMap<>();

        idxMap.put("-", -1);
        for(int i = 0; i < enroll.length; i ++){
            idxMap.put(enroll[i], i);
        }

        for(int j = 0; j < seller.length; j ++ ){
            int idx = idxMap.get(seller[j]);
            dfs(idx, amount[j] * 100, referral);
        }
        return answer;
    }

    public void dfs(int i, int price, String[] referral){
        answer[i] +=  (int) Math.ceil((price * 0.9));
        int idx = idxMap.get(referral[i]);
        if (idx == -1 || (int) price * 0.1 <= 0 ){
            return;
        }
        dfs(idx, (int) (price * 0.1), referral);
    }
}