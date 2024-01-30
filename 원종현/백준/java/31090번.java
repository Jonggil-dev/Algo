import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        for(int i=0;i<n;i++){
            String now = br.readLine();
            if((Integer.parseInt(now)+1)%Integer.parseInt(now.substring(2,4))!=0){
                System.out.println("Bye");
            }else{
                System.out.println("Good");
            }
        }
        
    }
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}