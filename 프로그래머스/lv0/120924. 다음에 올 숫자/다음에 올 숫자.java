import java.util.*;
class Solution {
    public int solution(int[] common) {
        int answer = 0;
        
        // 등차수열 -> 연속하는 수의 '차'가 일정
        if( (common[1] - common[0]) == (common[2] - common[1]) ){
            // answer = 공차 + 마지막 숫자
            answer = (common[1] - common[0]) + common[common.length-1];
        }
        
        // 등비수열 -> 연속하는 수의 '비율'이 일정
        else{
            // answer = 공비 * 마지막 숫자
            answer = (common[1] / common[0]) * common[common.length-1];
        }
        return answer;
    }
}