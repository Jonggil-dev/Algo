package 원종현.SWEA;

import java.io.*;
import java.util.*;

// SWEA
class Solution
{
    static int[][] graph;
    static int[][] parent;
    static int[] depth;
    static int N;
    static Set<Integer> sets;
	public static void main(String args[]) throws Exception
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int tc= Integer.parseInt(br.readLine());
        for(int sc=1;sc<=tc;sc++){
            String[] s= br.readLine().split(" ");
            int V=Integer.parseInt(s[0]);
            int E=Integer.parseInt(s[1]);
            int A=Integer.parseInt(s[2]);
            int B=Integer.parseInt(s[3]);
            graph = new int[V+1][2];
            parent = new int[V+1][20];
            depth = new int[V+1];
            sets = new HashSet<>();
            for(int i=1;i<=V;i++){
                sets.add(i);
            }
            String[] t=br.readLine().split(" ");
            for(int i=0;i<t.length;i+=2){
                int mom=Integer.parseInt(t[i]);
                int son=Integer.parseInt(t[i+1]);
                sets.remove(son);
                if(graph[mom][0]==0){
                    graph[mom][0]=son;
                }else{
                    graph[mom][1]=son;
                }
            }
            dfs(sets.iterator().next(),0);
            for(int j=1;j<20;j++){
                for(int i=1;i<=V;i++){
                    parent[i][j]=parent[parent[i][j-1]][j-1];
                }
            }
            int com=lca(A,B);

            bw.write('#'+Integer.toString(sc)+" "+Integer.toString(com)+" "+Integer.toString(sons(com))+'\n');
        }
        
        bw.flush();
	}
    static void dfs(int x,int d){
        depth[x]=d;
        for(int y:graph[x]){
            if(y==0){continue;}
            if(depth[y]==0){
                parent[y][0]=x;
                dfs(y,d+1);
            }
        }
    }
    static int sons(int x){
        int tmp=1;
        if(graph[x][0]!=0){
            tmp+=sons(graph[x][0]);
        }
        if(graph[x][1]!=0){
            tmp+=sons(graph[x][1]);
        }
        return tmp;
    }
    static int lca(int a,int b){
        if(depth[a]<depth[b]){
            int temp=a;
            a=b;
            b=temp;
        }
        for(int i=19;i>=0;i--){
            if(depth[a]-depth[b]>=(1<<i)){
                a=parent[a][i];
            }
        }
        if(a==b){return a;}
        for(int i=19;i>=0;i--){
            if(parent[a][i]!=parent[b][i]){
                a=parent[a][i];
                b=parent[b][i];
            }
        }
        return parent[a][0];
    }
}