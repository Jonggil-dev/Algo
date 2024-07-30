import java.util.*;

class Solution {
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        int r = board.length;
        int c = board[0].length;
        int[][] prefix = new int[r + 1][c + 1];

        for(int [] order : skill){
            if(order[0] == 1){
                prefix[order[1]][order[2]] += -order[5];
                prefix[order[1]][order[4] + 1] += order[5];
                prefix[order[3] + 1][order[2]] += order[5];
                prefix[order[3] + 1][order[4] + 1] += -order[5];
            } else {
                prefix[order[1]][order[2]] += order[5];
                prefix[order[1]][order[4] + 1] += -order[5];
                prefix[order[3] + 1][order[2]] += -order[5];
                prefix[order[3] + 1][order[4] + 1] += order[5];
            }
        }


        for(int i = 0 ; i < r; i ++){
            for(int j = 0 ; j < c - 1; j ++){
                prefix[i][j + 1] += prefix[i][j];
            }
        }

        for(int j = 0 ; j < c; j ++){
            for(int i = 0 ; i < r - 1; i ++){
                prefix[i + 1][j] += prefix[i][j];
            }
        }

        for(int i = 0 ; i < r; i ++){
            for(int j = 0 ; j < c; j ++){
                if(board[i][j] + prefix[i][j] > 0){
                    answer += 1;
                }
            }
        }

        return answer;
    }
}
