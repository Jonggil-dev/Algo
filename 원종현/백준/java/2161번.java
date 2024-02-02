import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N= Integer.parseInt(br.readLine());
        Deque<Integer> deque = new ArrayDeque<Integer>();
        for(int i=1; i<=N;i++){
            deque.addLast(i);
        }
        while(deque.size()>=1){
            System.out.print(deque.removeFirst());
            if(deque.size()>=1){
                System.out.printf(" ");
                deque.addLast(deque.removeFirst());
            }
        }
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}
