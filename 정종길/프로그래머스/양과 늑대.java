import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[] info, int[][] edges) {
        int answer = 0;
        List<ArrayList<Integer>> graph = IntStream.range(0,18).mapToObj(i -> new ArrayList<Integer>()).collect(Collectors.toList());

        for(int [] edge : edges){
            graph.get(edge[0]).add(edge[1]);
        }

        Queue<Object[]> q = new LinkedList<>();

        q.add(new Object[]{0, 1, 0, new ArrayList<>(graph.get(0))});

        while(!q.isEmpty()){
            Object[] data = q.poll();
            int now = (int) data[0];
            int sheep = (int) data[1];
            int wolf = (int) data[2];
            ArrayList<Integer> nextList = (ArrayList<Integer>) data[3];

            if(sheep > answer){
                answer = sheep;
            }

            for(int next : nextList){
                if(info[next] == 1){
                    if(sheep - (wolf + 1) > 0){
                        ArrayList<Integer> nnextList = new ArrayList<>(nextList);
                        nnextList.remove(Integer.valueOf(next));
                        nnextList.addAll(new ArrayList(graph.get(next)));
                        q.add(new Object[]{ next, sheep, wolf + 1, nnextList});
                    }

                } else {
                    ArrayList<Integer> nnextList = new ArrayList<>(nextList);
                    nnextList.remove(Integer.valueOf(next));
                    nnextList.addAll(new ArrayList(graph.get(next)));
                    q.add(new Object[]{ next, sheep + 1, wolf, nnextList});
                }
            }
        }
        return answer;
    }
}