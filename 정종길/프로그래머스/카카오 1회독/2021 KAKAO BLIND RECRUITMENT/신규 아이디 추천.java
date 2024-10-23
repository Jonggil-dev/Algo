import java.util.*;

class Solution {
    public String solution(String new_id) {
        String answer = "";
        String tmp = "";

        new_id = new_id.toLowerCase();
        new_id = new_id.replaceAll("[^a-z0-9-_.]", "");
        new_id = new_id.replaceAll("\\.{2,}", ".");
        new_id = new_id.replaceAll("^\\.|\\.$", "");
        if(new_id.length() == 0){
            new_id += 'a';
        };

        if(new_id.length() >= 16){
            for(int i = 0; i < 15; i ++){
                tmp += new_id.charAt(i);
            }
            tmp = tmp.replaceAll("\\.$", "");
        }else{
            tmp = new_id;
        };

        if(tmp.length() <= 2){
            answer = tmp;
            for(int i = tmp.length(); i < 3; i++ ){
                answer += tmp.charAt(tmp.length() - 1);
            }
        }else{
            answer = tmp;
        }

        return answer;
    }
}