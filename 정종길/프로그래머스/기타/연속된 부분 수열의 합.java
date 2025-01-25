import java.util.*;

class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = {};

        int i = 0;
        int j = 0;
        int tot = sequence[i];

        while(j < sequence.length){
            if (tot == k){
                if (answer.length == 0){
                    answer = new int[]{i, j};
                } else {
                    if((j - i) < (answer[1] - answer[0])){
                        answer = new int[]{i, j};
                    }
                }

                if (j == sequence.length - 1){
                    break;
                }

                j += 1;
                tot += sequence[j];


            } else if(tot < k){
                if (j == sequence.length - 1){
                    break;
                }

                j += 1;
                tot += sequence[j];

            } else{
                tot -= sequence[i];
                i += 1;
            }
        }

        return answer;
    }
}