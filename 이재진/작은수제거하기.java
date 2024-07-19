class Solution {
    public int[] solution(int[] arr) {
        int[] answer = new int[arr.length - 1];
        int min_num = 2147483647;
        for (int num:arr) {
            if (min_num > num) {
                min_num = num;
            }
        }
        int now = 0;
        for (int num:arr) {
            if (num != min_num) {
                answer[now] = num;
                now += 1;
            }
        }
        if (answer.length == 0) {
            int[] ans = {-1};
            return ans;
        }
        return answer;
    }
}
