class Solution {
    public String solution(String s) {
        String answer = "";
        int max=-99999999;
        int min=99999999;
        for(String num:s.split(" ")){
            int val=Integer.parseInt(num);
            if(val>max){max=val;}
            if(val<min){min=val;}
        }
        answer+=Integer.toString(min)+" "+Integer.toString(max);
        return answer;
    }
}