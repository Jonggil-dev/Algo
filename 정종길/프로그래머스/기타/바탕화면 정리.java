class Solution {
    public int[] solution(String[] wallpaper) {
        int si = -1, sj = -1, ei = -1, ej = -1;
        int row = wallpaper.length;
        int col = wallpaper[0].length();

        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(si == -1 && wallpaper[i].charAt(j) == '#'){
                    si = i;
                    break;
                }
            }
        }

        for(int j = 0; j < col; j++){
            for(int i = 0; i < row; i++){
                if(sj == -1 && wallpaper[i].charAt(j) == '#'){
                    sj = j;
                    break;
                }
            }
        }


        for(int i = row - 1; 0 <= i ; i--){
            for(int j = col - 1 ; 0 <= j; j--){
                if(ei == -1 && wallpaper[i].charAt(j) == '#'){
                    ei = i + 1;
                    break;
                }
            }
        }


        for(int j = col - 1 ; 0 <= j; j--){
            for(int i = row - 1; 0 <= i ; i--){
                if(ej == -1 && wallpaper[i].charAt(j) == '#'){
                    ej = j + 1;
                    break;
                }
            }
        }

        int[] answer = {si, sj, ei, ej};
        return answer;
    }
}