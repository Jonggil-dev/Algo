import java.util.*;

class Solution {
    public int solution(int[] nums) {
        
        Set<Integer> w = new HashSet<>(Arrays.asList(nums));
        
        int answer = 0;
        int n = (int) nums.length/2;
        Map<Integer, Integer> m = new HashMap<>();
        for (int i=0; i<nums.length; i++) {
            if (m.keySet().contains(nums[i])) {
                m.put(nums[i], m.get(nums[i]+1));
            } else {
                m.put(nums[i], 1);
            }
        }
        System.out.println(m.keySet().size());
        if (m.keySet().size() >= n) {
            answer = n;
        } else {
            answer = m.keySet().size();
        }
        return answer;
    }
}
