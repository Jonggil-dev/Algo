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
            String res = "OFF";
            String[] li = br.readLine().split(" ");
            int N=Integer.parseInt(li[0]);
            int M=Integer.parseInt(li[1]);
            int X=(1<<N)-1;
            if((M&X)==X){
                res="ON";
            }
            System.out.println("#"+i+" "+res);
        }
	}
}