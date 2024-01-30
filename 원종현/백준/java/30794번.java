import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        String s = st.nextToken();
        int res = 0;
        if(s.equals("bad")){res=n*200;}
        else if(s.equals("cool")){res=n*400;}
        else if(s.equals("great")){res=n*600;}
        else if(s.equals("perfect")){res=n*1000;}
        System.out.println(res);
        
    }
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}