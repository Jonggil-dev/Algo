package 원종현.SWEA;

import java.io.*;
import java.util.*;

// SWEA
class Solution
{
    static String[] tree;
    static int[] ltree;
    static int[] rtree;
    
    static int N;
	public static void main(String args[]) throws Exception
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int tc= 10;
        for(int sc=1;sc<=tc;sc++){
            N=Integer.parseInt(br.readLine());
            tree = new String[N+1];
            ltree = new int[N+1];
            rtree = new int[N+1];
            for(int i=0;i<N;i++){
                String[] s =br.readLine().split(" ");
                int num=Integer.parseInt(s[0]);
                String word=s[1];
                tree[num]=word;
                if(s.length==4){
                    ltree[num]=Integer.parseInt(s[2]);
                    rtree[num]=Integer.parseInt(s[3]);
                }else if(s.length==3){
                    ltree[num]=Integer.parseInt(s[2]);
                }
            }
            bw.write('#'+Integer.toString(sc)+" "+func(1)+'\n');
        }
        
        bw.flush();
	}
    static String func(int now){
        String tmp=tree[now];
        if(ltree[now]!=0){
            tmp=func(ltree[now])+tmp;

        }
        if(rtree[now]!=0){
            tmp=tmp+func(rtree[now]);
        }
        return tmp;
    }
}