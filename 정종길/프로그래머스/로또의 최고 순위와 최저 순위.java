import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer;
        int right = 0;
        List<Integer> li = Arrays.stream(win_nums).boxed().collect(Collectors.toList());

        int cnt = count(0, lottos);

        for(int num : lottos){
            if(li.indexOf(num) != -1){
                right += 1;
            }
        }

        if(right == 0){
            if(cnt == 0){
                answer = new int[] {6, 6};
            }
            else{
                answer = new int[] {7 - (cnt), 6};
            }

        }else {
            answer = new int[] {7 - (right + cnt), 7 - right};
        }
        return answer;
    }

    public int count(int num, int[] lottos){
        int cnt = 0;
        for(int lotto : lottos){
            if(num == lotto){
                cnt += 1;
            }
        }
        return cnt;
    }
}