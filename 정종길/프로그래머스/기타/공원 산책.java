class Solution {
    public int[] solution(String[] park, String[] routes) {

        int row = park.length;
        int column = park[0].length();

        int [] start = find_start(park);
        int r = start[0];
        int c = start[1];

        int[][] delta = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};


        for(String route:routes){
            char direction = route.charAt(0);
            int cnt = Character.getNumericValue(route.charAt(2));

            for(int i = 0; i < cnt; i++){
                if(direction == 'E') {
                    if(c + 1 < column && (park[r].charAt(c + 1) != 'X')){
                        c += 1;
                    }else{
                        c -= i;
                        break;
                    }

                } else if(direction == 'S') {
                    if(r + 1  < row && (park[r + 1].charAt(c) != 'X')){
                        r += 1;
                    }else{
                        r -= i;
                        break;
                    }

                }else if(direction == 'W'){
                    if(0 <= c - 1 && (park[r].charAt(c - 1) != 'X')){
                        c -= 1;
                    }else{
                        c += i;
                        break;
                    }

                }else if(direction == 'N'){
                    if(0 <= r - 1 &&  (park[r - 1].charAt(c) != 'X')){
                        r -= 1;
                    }else{
                        r += i;
                        break;
                    }
                }
            }
        }

        int[] answer = {r, c};

        return answer;
    }

    private int[] find_start(String[] park){
        for(int i = 0; i < park.length; i++){
            for(int j = 0; j < park[0].length(); j++){
                if(park[i].charAt(j) == 'S'){
                    return new int[] {i, j};
                }
            }
        }
        return new int[] {0, 0};
    }
}