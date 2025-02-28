import java.util.*;

class Solution {

    String[][] arrs; 
    int[] parents;      
    List<String> answer; 
    
    public List<String> solution(String[] commands) {
        answer = new ArrayList<>();
        arrs = new String[51][51];
        parents = new int[2501];

        for (int i = 1; i <= 2500; i++) {
            parents[i] = i;
        }

        for (String command : commands) {
            String[] li = command.split(" ");
            if (li[0].equals("UPDATE")) {
                if (li.length == 4) {
                    update_rc(Integer.parseInt(li[1]), Integer.parseInt(li[2]), li[3]);
                } else {
                    update_v(li[1], li[2]);
                }
            } else if (li[0].equals("MERGE")) {
                merge(Integer.parseInt(li[1]), Integer.parseInt(li[2]),
                      Integer.parseInt(li[3]), Integer.parseInt(li[4]));
            } else if (li[0].equals("UNMERGE")) {
                unmerge(Integer.parseInt(li[1]), Integer.parseInt(li[2]));
            } else {
                pprint(Integer.parseInt(li[1]), Integer.parseInt(li[2]));
            }
        }

        return answer;
    }

    private int rcToIndex(int r, int c) {
        return (r - 1) * 50 + c;
    }

    private int[] indexToRC(int idx) {
        int r = (idx - 1) / 50 + 1;
        int c = (idx - 1) % 50 + 1;
        return new int[] { r, c };
    }

    private int find_parents(int idx) {
        if (parents[idx] != idx) {
            parents[idx] = find_parents(parents[idx]);
        }
        return parents[idx];
    }

    private void merge(int r1, int c1, int r2, int c2) {
        int idx1 = rcToIndex(r1, c1);
        int idx2 = rcToIndex(r2, c2);

        int rep1 = find_parents(idx1);
        int rep2 = find_parents(idx2);

        if (rep1 == rep2) {
            return;
        }

        int[] rc1 = indexToRC(rep1);
        int[] rc2 = indexToRC(rep2);

        parents[rep2] = rep1;

        String value1 = arrs[rc1[0]][rc1[1]];
        String value2 = arrs[rc2[0]][rc2[1]];

        if (value1 != null && value2 != null) {
            arrs[rc2[0]][rc2[1]] = null;
        } else if (value1 == null && value2 != null) {
            arrs[rc1[0]][rc1[1]] = value2;
            arrs[rc2[0]][rc2[1]] = null;
        } else if (value1 != null && value2 == null) {
            arrs[rc2[0]][rc2[1]] = null;
        }
    }

    private void unmerge(int r, int c) {
        int targetIdx = rcToIndex(r, c);

        for (int i = 1; i <= 2500; i++) {
            find_parents(i);
        }

        int rep = find_parents(targetIdx);
        int[] repRC = indexToRC(rep);
        String savedValue = arrs[repRC[0]][repRC[1]];


        for (int i = 1; i <= 2500; i++) {
            if (find_parents(i) == rep) {
                parents[i] = i;
                if (i != targetIdx) {
                    int[] cellRC = indexToRC(i);
                    arrs[cellRC[0]][cellRC[1]] = null;
                }
            }
        }

        arrs[repRC[0]][repRC[1]] = null;
        arrs[r][c] = savedValue;
    }

    private void update_rc(int r, int c, String v) {
        int idx = rcToIndex(r, c);
        int rep = find_parents(idx);
        int[] repRC = indexToRC(rep);
        arrs[repRC[0]][repRC[1]] = v;
    }

    private void update_v(String v1, String v2) {
        for (int i = 1; i <= 50; i++) {
            for (int j = 1; j <= 50; j++) {
                if (arrs[i][j] != null && arrs[i][j].equals(v1)) {
                    arrs[i][j] = v2;
                }
            }
        }
    }

    private void pprint(int r, int c) {
        int idx = rcToIndex(r, c);
        int rep = find_parents(idx);
        int[] repRC = indexToRC(rep);
        if (arrs[repRC[0]][repRC[1]] == null) {
            answer.add("EMPTY");
        } else {
            answer.add(arrs[repRC[0]][repRC[1]]);
        }
    }
}
