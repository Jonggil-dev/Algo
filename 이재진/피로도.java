class Solution {
    public boolean[] visited;
    public int maxCount;
    
    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];
        maxCount = 0;
        dfs(k,dungeons,0);
        return maxCount;
    }
    
    public void dfs(int k, int[][] dungeons, int count) {
        maxCount = Math.max(maxCount, count);
        
        for (int i=0; i<dungeons.length; i++) {
            int req = dungeons[i][0];
            int use = dungeons[i][1];
            
            if (!visited[i] && k >= req) {
                visited[i] = true;
                dfs(k-use, dungeons, count+1);
                visited[i] = false;
            }
            
        }
    }
}
