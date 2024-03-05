import java.io.*;
import java.util.*;

// SWEA
class Main {
    static int[] depth;
    static ArrayList<Integer>[] graph;
    static int[][] parent;
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        parent = new int[N+1][20];
        depth = new int[N+1];
        graph = new ArrayList[N+1];
        for(int i=0;i<=N;i++){
            graph[i]= new ArrayList<Integer>();
        }
        int a,b;
        for(int i=0;i<N-1;i++){
            String[] tmp=br.readLine().split(" ");
            a=Integer.parseInt(tmp[0]);
            b=Integer.parseInt(tmp[1]);
            graph[a].add(b);
            graph[b].add(a);
        }
        dfs(1,0);
        for(int j=1;j<20;j++){
            for(int i=1;i<=N;i++){
                parent[i][j]=parent[parent[i][j-1]][j-1];
            }
        }
        int M = Integer.parseInt(br.readLine());
        for(int i=0;i<M;i++){
            String[] tmp =br.readLine().split(" ");
            a=Integer.parseInt(tmp[0]);
            b=Integer.parseInt(tmp[1]);
            bw.write(Integer.toString(lca(a,b))+"\n");
        }
        
        bw.flush();
    }

    static void dfs(int x,int par){
        for(int y:graph[x]){
            if(y==par){
                continue;
            }
            depth[y]=depth[x]+1;
            parent[y][0]=x;
            dfs(y,x);
        }
    }

    static int lca(int a,int b){
        if(depth[a]<depth[b]){
            int tmp=a;
            a=b;
            b=tmp;
        }
        for(int i=19;i>=0;i--){
            if(depth[a]-depth[b]>=1<<i){
                a=parent[a][i];
            }
        }
        if(a==b){
            return a;
        }
        System.out.println(Integer.toString(a)+"-"+Integer.toString(b));
        for(int i=19;i>=0;i--){
            if(parent[a][i]!=parent[b][i]){
                a=parent[a][i];
                b=parent[b][i];
            }
        }
        return parent[a][0];
    }
}
