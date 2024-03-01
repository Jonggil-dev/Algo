package 원종현.SWEA;

import java.io.*;
import java.util.*;

// SWEA
class Solution
{
	public static void main(String args[]) throws Exception
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int tc= Integer.parseInt(br.readLine());
        for(int sc=1;sc<=tc;sc++){
            String[] tmp = br.readLine().split(" ");
            int N = Integer.parseInt(tmp[0]);
            int M = Integer.parseInt(tmp[1]);
            int L = Integer.parseInt(tmp[2]);
            tmp=br.readLine().split(" ");
            LinkedList<Integer> l=new LinkedList<Integer>();
            for(int i=0;i<N;i++){l.add(Integer.parseInt(tmp[i]));}
            for(int i=0;i<M;i++){
                String[] t = br.readLine().split(" ");
                if(t[0].equals("I")){
                    l.add(Integer.parseInt(t[1]),Integer.parseInt(t[2]));
                }else if(t[0].equals("D")){
                    l.remove(Integer.parseInt(t[1]));
                }else{
                    l.set(Integer.parseInt(t[1]),Integer.parseInt(t[2]));
                }
            }
            if(l.size()<=L){
                bw.write("#"+Integer.toString(sc)+" -1\n");
            }else{
            bw.write("#"+Integer.toString(sc)+" "+Integer.toString(l.get(L))+"\n");
        }
        }
        
        bw.flush();
	}
}