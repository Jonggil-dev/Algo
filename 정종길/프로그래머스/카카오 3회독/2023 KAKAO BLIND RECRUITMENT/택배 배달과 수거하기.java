import java.util.*;

class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        int dEnd = -1, pEnd = -1;
        
        for(int i = n - 1; i >= 0; i--){
            if(deliveries[i] != 0){
                dEnd = i;
                break;
            }
        }
        
        for(int j = n - 1; j >= 0; j--){
            if(pickups[j] != 0){
                pEnd = j;
                break;
            }
        }

        while(dEnd != -1 || pEnd != -1) {
            answer += (Math.max(dEnd, pEnd) + 1) * 2;
            int dcap = cap;
            
            while(dEnd != -1){
                if(deliveries[dEnd] > dcap){
                    deliveries[dEnd] -= dcap;
                    break;
                    
                } else {
                    dcap -= deliveries[dEnd];
                    deliveries[dEnd] = 0;
                }
                
                while(dEnd != -1 && deliveries[dEnd] == 0){
                    dEnd -= 1;
                }
            }
            
            int pcap = cap;
            while(pEnd != -1){
                if(pickups[pEnd] > pcap){
                    pickups[pEnd] -= pcap;
                    break;

                } else {
                    pcap -= pickups[pEnd];
                    pickups[pEnd] = 0;
                }

                while(pEnd != -1 && pickups[pEnd] == 0){
                    pEnd -= 1;
                }
            }
        }
        
        return answer;
    }
}