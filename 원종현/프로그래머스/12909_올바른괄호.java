import java.util.Stack;
class Solution {
    boolean solution(String s) {
        boolean answer = false;
        Stack<Character> stk=new Stack<>();
        for(int i=0;i<s.length();i++){
            char now=s.charAt(i);
            if(stk.empty()||stk.peek()==now){
                stk.push(now);
            }else if(!stk.empty()&&stk.peek()!=now&&now==')'){
                stk.pop();
            }
        }
        if(stk.empty()){
            answer=true;
        }
        return answer;
    }
}