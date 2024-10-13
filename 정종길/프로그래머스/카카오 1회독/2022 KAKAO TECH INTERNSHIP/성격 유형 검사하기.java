import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        HashMap<String, Integer> records = new HashMap<>();

        for(int i = 0; i < choices.length; i ++){
            int choice = choices[i];
            if(choice <= 3){
                String key = "" + survey[i].charAt(0);
                records.put(key, records.getOrDefault(key, 0) + 4 - choice);
            }else if ( 5 <= choice && choice <= 7){
                String key = "" + survey[i].charAt(1);
                records.put(key, records.getOrDefault(key, 0) + choice - 4);
            }
        }

        StringBuilder answer = new StringBuilder();
        answer.append(records.getOrDefault("R", 0) >= records.getOrDefault("T", 0) ? "R" : "T");
        answer.append(records.getOrDefault("C", 0) >= records.getOrDefault("F", 0) ? "C" : "F");
        answer.append(records.getOrDefault("J", 0) >= records.getOrDefault("M", 0) ? "J" : "M");
        answer.append(records.getOrDefault("A", 0) >= records.getOrDefault("N", 0) ? "A" : "N");

        return answer.toString();
    }
}