package 원종현.SWEA;

import java.io.*;
import java.util.*;

// SWEA
class Solution
{
	public static void main(String args[]) throws Exception
	{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int tc= 10;
        int res = 0;
        for(int sc=1;sc<=tc;sc++){
            int N = Integer.parseInt(br.readLine());
            LinkedList<Integer> li = new LinkedList<Integer>();
            String[] tmp = br.readLine().split(" ");
            for(int i=0;i<N;i++){li.add(Integer.parseInt(tmp[i]));}
            int M= Integer.parseInt(br.readLine());
            String[] tmp2 = br.readLine().split(" ");
            LinkedList<String> orders = new LinkedList<String>();
            int idx=0;
            while(idx<tmp2.length){
                orders.add(tmp2[idx]);
                idx++;
            }
            while(true){
                String order = orders.pop();
                if (order.equals("I")){
                    int x = Integer.parseInt(orders.pop());
                    int y = Integer.parseInt(orders.pop());
                    for(int k=x;k<x+y;k++){
                        li.add(k,Integer.parseInt(orders.pop()));
                    }
                }
                else if(order.equals("D")){
                    int x = Integer.parseInt(orders.pop());
                    int y = Integer.parseInt(orders.pop());
                    for(int k=0;k<y;k++){
                        li.remove(x);
                    }
                }else{
                    int y = Integer.parseInt(orders.pop());
                    for(int k=0;k<y;k++){
                        li.add(Integer.parseInt(orders.pop()));
                    }
                }
                if(orders.isEmpty()){
                    break;
                }
            }
            bw.write("#"+Integer.toString(sc));
            for(int i=0;i<10;i++){
                bw.write(" ");
                bw.write(Integer.toString(li.pop()));
            }
            bw.newLine();

        }
        bw.flush();
	}
}