import java.util.*;

class Solution {
    static int[] answer;
    static int maxDiff;

    public int[] solution(int n, int[] info) {
        int apeach = 0;
        maxDiff = 0;
        answer = null;

        for (int i = 0; i < 11; i++) {
            if (info[i] != 0) {
                apeach += (10 - i);
            }
        }

        dfs(n, 0, apeach, new int[11], info);

        if (answer == null) {
            return new int[] { -1 };
        }
        return answer;
    }

    public void dfs(int n, int lion, int apeach, int[] scores, int[] info) {
        if (n == 0) {
            if (lion > apeach) {
                if (maxDiff <= (lion - apeach)) {
                    maxDiff = (lion - apeach);
                    answer = scores.clone();
                }
            }
            return;
        }

        for (int i = 0; i < 11; i++) {
            if (i == 10 && n >= 0) {
                scores[10] = n;
                dfs(0, lion, apeach, scores, info);
                scores[10] = 0;
                return;
            }

            if (scores[i] == 0 && n >= (info[i] + 1)) {
                scores[i] = info[i] + 1;
                if (info[i] != 0) {
                    dfs(n - scores[i], lion + (10 - i), apeach - (10 - i), scores, info);
                } else {
                    dfs(n - scores[i], lion + (10 - i), apeach, scores, info);
                }
                scores[i] = 0;
            }
        }
    }
}
