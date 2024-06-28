class Solution {
    boolean solution(String s) {
        boolean answer = false;
        int a=0;
        System.out.println("Hello Java");
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='y'||s.charAt(i)=='Y'){
                a++;
            }
            else if(s.charAt(i)=='p'||s.charAt(i)=='P'){
                a--;
            }
        }
        if(a==0){
            answer=true;
        }
        return answer;
    }
}