import java.util.*;

class Solution {
    public int[] solution(int[][] edges) {
        int[] answer = {0, 0, 0, 0};
        HashSet<Integer> rootCheck = new HashSet<>();
        List<List<Integer>> graph = new ArrayList<>();
        
        for(int i = 0; i < 1000001; i++){
            graph.add(new ArrayList<>());
        }
        
        for(int[] edge : edges){
            int s = edge[0];
            int e = edge[1];
            graph.get(s).add(e);
            rootCheck.add(e);
        }
        
        int root = findRoot(graph, rootCheck);
        answer[0] = root;
        
        for(Integer s : graph.get(root)){
            Deque<Integer> q = new ArrayDeque<>(Arrays.asList(s));
            HashSet<Integer> visited = new HashSet<>(Arrays.asList(s));
            int cnt = 0;
                
            while(!q.isEmpty()){
                int here = q.pollFirst();
                for(Integer next : graph.get(here)){
                        cnt += 1;
                        if(!visited.contains(next)){
                            visited.add(next);
                            q.add(next);
                    }
                }
            }

            if(visited.size() - 1 == cnt){
                answer[2] += 1;
            }else if(visited.size() == cnt) {
                answer[1] += 1;
            }else{
                answer[3] += 1;
            }
            
        }
        
        return answer;
    }
    
    private int findRoot(List<List<Integer>> graph, HashSet<Integer> rootCheck){
        int root = 0;
        for(int i= 1; i < 1000000; i++ ){
            if(graph.get(i).size() >= 2){
                if(!rootCheck.contains(i)){
                    root = i;
                }
            }
        }
        return root;
    }
}