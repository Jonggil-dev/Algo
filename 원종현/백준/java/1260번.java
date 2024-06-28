import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static boolean[] visit;
    static int[][] graph;
    static int N,M,V;
    static String res="";
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());
        graph=new int[N+1][N+1];
        visit= new boolean[N+1];
        for(int i=0;i<M;i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a][b]=1;
            graph[b][a]=1;
        }
        
        dfs(V);
        System.out.println(res);
        visit= new boolean[N+1];
        res="";
        bfs(V);
        System.out.println(res);
    }

    public static void dfs(int st){
        visit[st]=true;
        res+=st+" ";
        for(int i=0;i<=N;i++){
            if(graph[st][i]==1&&!visit[i]){
                dfs(i);
            }
        }
    }

    public static void bfs(int st){
        Queue<Integer> q = new LinkedList<>();
        q.add(st);
        visit[st]=true;
        while(!q.isEmpty()){
            int now=q.poll();
            res+=now+" ";
            for(int i=0;i<=N;i++){
                if(graph[now][i]==1&&!visit[i]){
                    q.add(i);
                    visit[i]=true;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}
