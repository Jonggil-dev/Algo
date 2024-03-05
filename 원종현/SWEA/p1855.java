package 원종현.SWEA;
import java.io.*;
import java.util.*;

// SWEA
class Solution {
    static int[] depth;
    static ArrayList<Integer>[] graph;
    static int[][] parent;
    static int N;
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int tc= Integer.parseInt(br.readLine());
        for(int sc=1;sc<=tc;sc++){
        N = Integer.parseInt(br.readLine());
        parent = new int[N+1][20];
        depth = new int[N+1];
        graph = new ArrayList[N+1];
        for(int i=0;i<=N;i++){
            graph[i]= new ArrayList<Integer>();
        }
        String[] nodes=br.readLine().split(" ");
        int pa,son;
        for(int i=1;i<N;i++){
            son=i+1;
            pa=Integer.parseInt(nodes[i-1]);
            graph[pa].add(son);
        }
        dfs();
        for(int j=1;j<20;j++){
            for(int i=1;i<=N;i++){
                parent[i][j]=parent[parent[i][j-1]][j-1];
            }
        }
        
        bw.write("#"+Integer.toString(sc)+" "+Long.toString(bfs())+"\n");
        }
        bw.flush();
    }

    static void dfs(){
        Deque<Integer> stack = new ArrayDeque<>(); // 노드를 저장할 스택
        stack.push(1); // 시작 노드를 스택에 푸시
        depth[1] = 1; // 루트 노드의 깊이는 1로 설정
        while (!stack.isEmpty()) {
            int node = stack.pop(); // 현재 노드
    
            for (int child : graph[node]) { 
                if (child != parent[node][0]) { 
                    parent[child][0] = node; 
                    depth[child] = depth[node] + 1; 
                    stack.push(child);
                }
            }
        }
    }

    static int lca(int a,int b){
        if(depth[a]<depth[b]){
            int tmp=a;
            a=b;
            b=tmp;
        }
        int oa=a;
        int ob=b;
        for(int i=19;i>=0;i--){
            if(depth[a]-depth[b]>=1<<i){
                a=parent[a][i];
            }
        }
        if(a==b){
            return depth[oa]-depth[ob];
        }
        for(int i=19;i>=0;i--){
            if(parent[a][i]!=parent[b][i]){
                a=parent[a][i];
                b=parent[b][i];
            }
        }
        return (depth[ob]+depth[oa])-2*depth[parent[a][0]];
    }

    static Long bfs(){
        boolean[] visit=new boolean[N+1];
        ArrayList<Integer> course=new ArrayList<Integer>();
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        course.add(1);
        visit[1]=true;
        while(!q.isEmpty()){
            int now = q.poll();
            for(int i:graph[now]){
                if(!visit[i]){
                    visit[i]=true;
                    q.add(i);
                    course.add(i);
                }
            }
        }
        Long res=0L;
        for(int i=0;i<course.size()-1;i++){
            res+=lca(course.get(i),course.get(i+1));
            //System.out.printf("%d -> %d = %d \n",course.get(i),course.get(i+1),lca(course.get(i),course.get(i+1)));
        }
        return res;
    }
}
