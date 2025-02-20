class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
            
        for(int i = 0; i < schedules.length; i ++ ){
            int sch = schedules[i] + 10;
            
            if(sch % 100 >= 60){
                sch = (((sch / 100) + 1) * 100) + (sch % 100 - 60);
            }
            
            int check = 0;
            
            for(int j = 0; j < 7; j++){
                int idx = (startday + j) % 7;
                
                if(idx == 6 || idx == 0){
                    check += 1;
                    continue;
                }
                

                int times = timelogs[i][j];
                if(times <= sch) {
                    check += 1;
                }                
            }
            
            if(check == 7){
                answer += 1;
            }
        }
            
        return answer;
    }
}