import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        
        int answer = 0;
        PriorityQueue<Integer> q = new PriorityQueue<>();
        for (int s:scoville) {
            q.offer(s);
        }
        while (true) {
            if (q.size() == 1) {
                int x = q.poll();
                if (x >= K) {
                    break;
                } else {
                    return -1;
                }
            }
            
            Boolean flag = false;
            for (int i:q) {
                if (i < K) {
                    flag = true;
                    break;
                }
            }
            if (flag) {
                int tmp = 0;
                tmp += q.poll();
                tmp += (q.poll()*2);
                q.offer(tmp);
                answer++;
            } else {
                break;
            }
        }
        return answer;
    }
}
