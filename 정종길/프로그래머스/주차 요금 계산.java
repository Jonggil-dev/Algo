import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int[] fees, String[] records) {
        ArrayList<Integer> answer = new ArrayList<>();
        TreeMap<String, List<String>> table = new TreeMap<>();

        for(String record: records){
            String[] rec = record.split(" ");
            String time = rec[0];
            String car = rec[1];

            if(table.containsKey(car)){
                table.get(car).add(time);

            }else{
                List<String> tmp = new ArrayList<>();
                tmp.add(time);
                table.put(car, tmp);
            }

        }

        for(String key : table.keySet()){
            int fee = cal_fee(table.get(key), fees, fees[0]);
            answer.add(fee);
        }

        return answer;
    }

    public int cal_fee(List<String> times, int[] fees, int basic) {

        int fee = 0;
        int time = 0;

        if(times.size() % 2 == 1){
            int out = 1439;
            int in = Integer.parseInt(times.get(times.size() - 1).substring(0, 2)) * 60 + Integer.parseInt(times.get(times.size() - 1).substring(3));
            time += out - in;
        }

        for(int i = 0; i < times.size() - 1; i += 2){
            int out = Integer.parseInt(times.get(i + 1).substring(0, 2)) * 60 + Integer.parseInt(times.get(i + 1).substring(3));
            int in = Integer.parseInt(times.get(i).substring(0, 2)) * 60 + Integer.parseInt(times.get(i).substring(3));
            time += out - in;
        }

        if(time - fees[0] > 0){
            fee += fees[1] + Math.ceil(((time - fees[0]) / (double)fees[2])) * fees[3];
        } else {
            fee += fees[1];
        }

        return fee;

    }
}