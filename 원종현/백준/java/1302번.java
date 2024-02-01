import java.io.*;
import java.util.*;

public class Main {

    public void solution() throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        HashMap<String, Integer> map = new HashMap<>();
        int res = -1;
        for(int i=0;i<N;i++){
            String s = br.readLine();
            if(map.containsKey(s)){
                map.put(s, map.get(s) + 1);
                }else{
                map.put(s,1);
            }
            res = Math.max(res, map.get(s));
        }
    
        
        List<String> li = new ArrayList<>();
        for (Map.Entry<String, Integer> e : map.entrySet()) {
            if (e.getValue() == res) li.add(e.getKey());
        }
        Collections.sort(li);
        System.out.print(li.get(0));
    }
        

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}