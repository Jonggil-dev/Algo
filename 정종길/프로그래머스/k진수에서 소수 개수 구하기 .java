import java.util.*;

class Solution {
    public int solution(int n, int k) {
        int answer = 0;

        String kBinaryNum = kBinary(n, k);
        String[] kBinaryNums = kBinaryNum.split("0");

        for(String num : kBinaryNums) {
            if(!num.isEmpty()){
                if(checkPrimeNumber(Long.parseLong(num))){
                    answer += 1;
                }
            }
        }

        return answer;
    }

    public String kBinary(int n, int k){
        String kNum = "";
        while(n != 0){
            kNum = (n % k) + kNum;
            n /= k;
        }
        return kNum;
    }

    public boolean checkPrimeNumber(long num) {
        if (num == 1){
            return false;
        }

        long sqrt = (long) Math.sqrt(num);
        for(int i = 2 ; i <= sqrt; i++) {
            if(num % i == 0) {
                return false;
            }
        }
        return true;
    }
}