import java.util.*;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int[] ls = new int[1000];
        for (int i:array) {
            ls[i] += 1;
        }
        List<Integer> arr = new ArrayList<>();
        int max_cnt = 0;
        for (int i=0; i<1000; i++) {
            if (max_cnt < ls[i]) {
                max_cnt = ls[i];
                answer = i;
                arr = new ArrayList<>();
                arr.add(i);
            } else if (max_cnt == ls[i]) {
                arr.add(i);
            }
        }
        if (arr.size() > 1) {
            return -1;
        }
        return answer;
    }
}
