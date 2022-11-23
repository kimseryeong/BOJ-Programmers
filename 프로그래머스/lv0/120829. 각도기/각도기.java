import java.util.*;

class Solution {
    public int solution(int angle) {
        int answer = 0;
        
        // 0~89 : 예각, 90 : 직각, 91~179 : 둔각, 180 : 평각
        if(angle > 0 && angle < 90){
            answer = 1;
        }else if(angle == 90){
            answer = 2;
        }else if(angle < 180){
            answer = 3;
        }else if(angle == 180){
            answer = 4;
        }
        
        return answer;
    }
}