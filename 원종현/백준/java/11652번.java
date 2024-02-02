import java.io.*;
import java.util.*;
import java.math.*;

public class Main {

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
     
        Map<BigInteger,Integer> dic = new HashMap<>();
        int N=Integer.parseInt(br.readLine());
        BigInteger res = new BigInteger("-1");
        int res2 = 0;
        for(int i=0;i<N;i++){
            BigInteger tmp =new BigInteger(br.readLine());
            if(dic.containsKey(tmp)){
                dic.put(tmp,dic.get(tmp)+1);
            }else{
                dic.put(tmp,1);
            }
        }
        for(Map.Entry<BigInteger,Integer> entry:dic.entrySet()){
            BigInteger key = entry.getKey();
            int val = entry.getValue();
            if(val>res2){
                res=key;
                res2=val;
            }else if(val==res2){
                if(key.compareTo(res)==-1){
                    res=key;
                    res2=val;
                }
            }
        }
        System.out.println(res);
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}
