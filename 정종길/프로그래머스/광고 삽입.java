import java.util.*;

class Solution {
    public String solution(String play_time, String adv_time, String[] logs) {
        int playSec = toSeconds(play_time);
        int advSec = toSeconds(adv_time);
        int[] records = new int[playSec + 1];

        for(String log : logs){
            String[] logLi = log.split("-");
            int startSec = toSeconds(logLi[0]);
            int endSec = toSeconds(logLi[1]);
            records[startSec] += 1;
            records[endSec] -= 1;
        }

        for(int i = 1; i < records.length; i ++){
            records[i] += records[i - 1];
        }


        int[] subLi = Arrays.copyOfRange(records, 0, advSec + 1);
        long maxRunningTime = Arrays.stream(subLi)
                .sum();

        int start_ad = 0;
        int end_ad = advSec;
        long runningTime = maxRunningTime;
        int answer = 0;

        for(int k = advSec + 1; k < playSec + 1; k++){
            runningTime -= records[start_ad];
            runningTime += records[k];
            start_ad += 1;
            if (maxRunningTime < runningTime){
                answer = start_ad;
                maxRunningTime = runningTime;
            }
        }

        String hour = String.format("%02d", answer / 3600);
        String min = String.format("%02d", (answer % 3600) / 60);
        String sec = String.format("%02d", (answer % 3600) % 60);

        return hour + ":" + min + ":" + sec;
    }

    public int toSeconds(String text){
        int sec = 0;
        String[] times = text.split(":");

        sec += Integer.parseInt(times[0]) * 3600 + Integer.parseInt(times[1]) * 60 + Integer.parseInt(times[2]);
        return sec;
    }
}