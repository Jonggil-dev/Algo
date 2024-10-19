class Solution {
    public int solution(int storey) {
        int answer = 0;
        while (storey != 0) {
            int x = storey%10;
            if (x == 0) {
                storey = (int) storey/10;
            } else if (x == 5) {
                if (storey % 100 == 0 || storey % 100 >= 50) {
                    storey += 10-x;
                    answer += 10-x;
                } else {
                    storey -= x;
                    answer += x;
                }
            } else if (x > 5) {
                storey += 10-x;
                answer += 10-x;
            } else {
                storey -= x;
                answer += x;
            }
            
        }
        return answer;
    }
}
