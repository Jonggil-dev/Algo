import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int res = 0 ;
        for(int i=0;i<8;i++){
            String now = br.readLine();
            for(int j=0;j<8;j++){
                char c = now.charAt(j);
                if(c=='p'){res+=1;}
                else if(c=='P'){res-=1;}
                else if(c=='n'){res+=3;}
                else if(c=='N'){res-=3;}
                else if(c=='b'){res+=3;}
                else if(c=='B'){res-=3;}
                else if(c=='r'){res+=5;}
                else if(c=='R'){res-=5;}
                else if(c=='q'){res+=9;}
                else if(c=='Q'){res-=9;}
                
            }
        }
        System.out.println(-res);
        
    }
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}