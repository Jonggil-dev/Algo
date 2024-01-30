import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int res = 0;
        for(int i=0; i<N;i++){
            int tmp =0;
            String line = br.readLine();
            for(int j=0;j<line.length();j++){
                if(line.charAt(j)=='O'){tmp++;}
            }
            if(tmp>=Math.ceil(M/2.0)){res++;}
        }
        System.out.println(res);

    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}
