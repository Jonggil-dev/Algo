class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = {};

        for(int i = 0; i < callings.length; i++){
            for(int j = 0; j < players.length; j++){
                if(players[j].equals(callings[i])){
                    players[j] = players[j - 1];
                    players[j - 1] = callings[i];
                    break;
                }
            }
        }
        return players;
    }
}