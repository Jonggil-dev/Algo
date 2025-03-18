import java.util.*;

class Solution {
    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        int[] answer = {0, Integer.MAX_VALUE};
        HashSet<Integer> hashSummits = changeSet(summits);
        HashSet<Integer> hashGates = changeSet(gates);
        List<List<int[]>> graph = new ArrayList<>();

        
        for(int i = 0; i < n + 1 ; i ++){
            graph.add(new ArrayList<>());
        }
                
        for(int[] path: paths){
            graph.get(path[0]).add(new int[]{path[1], path[2]});
            graph.get(path[1]).add(new int[]{path[0], path[2]});
        }
        
        PriorityQueue<Integer[]> q = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        int[] memo = new int[n + 1];
            
        for(int i = 0; i < n + 1; i++){
            memo[i] = Integer.MAX_VALUE;
        }
        
        for(int gate : gates){
            
            q.add(new Integer[] {0, gate});
        }
            
        while (!q.isEmpty()){
            Integer[] data = q.poll();
            int nowIntensity = data[0];
            int now = data[1];

            if(nowIntensity > answer[1]) {
                continue;
            }

            if(hashSummits.contains(now)){
                if(nowIntensity < answer[1]){
                    answer[0] = now;
                    answer[1] = nowIntensity;
                } else if (nowIntensity == answer[1]){
                    if(now < answer[0]){
                        answer[0] = now;
                        answer[1] = nowIntensity;
                    }
                }
                continue;
            }

            for(int[] nextData: graph.get(now)){
                int maxIntensity = Math.max(nowIntensity, nextData[1]);
                int nextNode = nextData[0];

                if(hashGates.contains(nextNode)){
                    continue;
                }

                if(maxIntensity < memo[nextNode]){
                    memo[nextNode] = maxIntensity;
                    q.add(new Integer[]{maxIntensity, nextNode});
                }
            }
        }
        
        return answer;
    }
    
    private HashSet<Integer> changeSet(int[] li){
        HashSet<Integer> hs = new HashSet<>();
        
        for(int l : li){
            hs.add(l);
        }
        
        return hs;
    }
}