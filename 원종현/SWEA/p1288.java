package 원종현.SWEA;
import java.io.*;
import java.util.*;

class p1288
{
	public static void main(String args[]) throws Exception
	{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc= Integer.parseInt(br.readLine());
        for(int i=1;i<=tc;i++){
            int N = Integer.parseInt(br.readLine());
            int T = 0;
            int r = 0;
            while(r!=1023){
                T+=N;
                String tmp = Integer.toString(T);
                for(int j=0;j<tmp.length();j++){
                    r|=(1<<(tmp.charAt(j)-'0'));
                }
            }
            System.out.println("#"+i+" "+T);
        }
	}
}