import java.util.*;
class Solution {
    public ArrayList<Integer> solution(String today, String[] terms, String[] privacies) {
        ArrayList<Integer> answer = new ArrayList<>();
        HashMap<String, Integer> termsMap = new HashMap<>();

        String[] s_today = today.split("\\.");
        ArrayList<Integer> i_today = new ArrayList<>();

        for(String data : s_today){
            i_today.add(Integer.parseInt(data));
        }


        for(String term: terms){
            String[] term_li = term.split(" ");
            termsMap.put(term_li[0], Integer.parseInt(term_li[1]));
        }

        for(int i = 0; i < privacies.length; i++){
            String[] divide = privacies[i].split(" ");
            String alpha = divide[1];

            String[] period = divide[0].split("\\.");
            int year = Integer.parseInt(period[0]);
            int month = Integer.parseInt(period[1]);
            int day = Integer.parseInt(period[2]);

            int d_year = (month + termsMap.get(alpha) - 1) / 12;
            int d_month = (month + termsMap.get(alpha)) % 12;

            if(d_month == 0){
                d_month = 12;
            }

            year += d_year;

            if(day == 1){
                if (d_month == 1){
                    year -= 1;
                    d_month = 12;
                } else {
                    d_month -= 1;
                };
                day = 28;

            }else{
                day -= 1;
            }

            if(year < i_today.get(0)){
                answer.add(i + 1);
                continue;

            } else if(year > i_today.get(0)){
                continue;
            }

            if(d_month < i_today.get(1)){
                answer.add(i + 1);
                continue;

            }else if(d_month > i_today.get(1)){
                continue;
            }

            if(day < i_today.get(2)){
                answer.add(i + 1);
                continue;
            }
        }

        return answer;
    }
}