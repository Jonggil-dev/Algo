import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int res = 0 ;
        int stat = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0;i<4;i++){
            stat+=Integer.parseInt(st.nextToken());
        }
        int n=Integer.parseInt(st.nextToken());
        res=Math.max(0,4*n-stat);
        System.out.println(res);
        
    }
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}