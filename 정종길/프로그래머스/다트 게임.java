class Solution {
    public int solution(String dartResult) {
        
        int answer = 0;
        int idx = 0;
        int prev_num = 0;
        while(idx < dartResult.length()){
            int num = Integer.parseInt(String.valueOf(dartResult.charAt(idx)));
            char txt = dartResult.charAt(idx + 1);
                
                if(Character.isDigit(txt)){
                    num = 10;
                    idx += 1;
                    txt = dartResult.charAt(idx + 1);
                }
                
                if(txt == 'D'){
                    num = num * num;
                }else if(txt == 'T'){
                    num = num * num * num;
                }
            

                answer += num;
            
                idx += 2;
                    
                if((idx) < dartResult.length() && !Character.isDigit(dartResult.charAt(idx))){
                    if(dartResult.charAt(idx) == '*'){
                        answer += (prev_num + num);
                        num = 2 * num;
                            
                    }else{
                        num = -1 * num;
                        answer += 2 * num;
                    }
                    idx += 1;
                }
            prev_num = num;
        }
        return answer;
    }
}