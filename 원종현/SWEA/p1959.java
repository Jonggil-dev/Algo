package 원종현.SWEA;
import java.io.*;
import java.util.*;

class Solution
{
	public static void main(String args[]) throws Exception
	{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc= Integer.parseInt(br.readLine());
        for(int i=1;i<=tc;i++){
            int res = 0;
            String[] li = br.readLine().split(" ");
            int N=Integer.parseInt(li[0]);
            int M=Integer.parseInt(li[1]);
            int[] A = new int[N];
            int[] B = new int[M];
            String[] tmp = br.readLine().split(" ");
            for(int j=0;j<N;j++){A[j]=Integer.parseInt(tmp[j]);}
            String[] tmp2 = br.readLine().split(" ");
            for(int j=0;j<M;j++){B[j]=Integer.parseInt(tmp2[j]);}
            for (int j=0;j<=Math.max(N,M)-Math.min(N,M);j++){
                int tmp3=0;
                if(N<=M){
                for(int k=0;k<N;k++){
                    tmp3+=A[k]*B[j+k];
                }
                }else{
                    for(int k=0;k<M;k++){
                        tmp3+=A[j+k]*B[k];
                    }
                }
                res=Math.max(res,tmp3);
            }
            System.out.println("#"+i+" "+Integer.toString(res));
        }
	}
}