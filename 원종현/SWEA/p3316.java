package 원종현.SWEA;

import java.io.*;
import java.util.*;

// SWEA
class Solution
{
    static int[][] dp;
    static String S;
	public static void main(String args[]) throws Exception
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int tc= Integer.parseInt(br.readLine());
        for(int sc=1;sc<=tc;sc++){
            S = br.readLine();
            dp= new int[S.length()+1][16];
            bw.write('#'+Integer.toString(sc)+" "+Integer.toString(func())+'\n');
        }
        
        bw.flush();
	}
    static int func(){
        dp[0][1]=1;
        for(int i=1;i<16;i++){
            if((i&(1<<S.charAt(0)-'A'))!=0&&((i&1)!=0)){
                dp[1][i]=1;
            }
        }
        for(int i=2;i<=S.length();i++){
            for(int j=1;j<16;j++){
                for(int k=1;k<16;k++){
                    if((j&(1<<S.charAt(i-1)-'A'))!=0&&((j&k)!=0)){
                        dp[i][j]+=dp[i-1][k];
                        dp[i][j]%=1000000007;
                    }
                }
            }
        }
        int res = 0;
        for(int i=1;i<16;i++){
            res+=dp[S.length()][i];
            res%=1000000007;
        }
        return res;
    }
}