import java.util.*;
class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        
        // 양꼬치 10인분 -> 음료수 1개 서비스
        // 양꼬치(n) : 12000, 음료수(k) : 2000
        
        // 10인분 미만
        if(n < 10){
            answer = n * 12000 + 2000 * k;
        }
        
        // 10인분 이상
        else{
            // 음료수 서비스 개수 == 양꼬치 n/10
            //  -> 총 음료수 개수 - 서비스 개수
            answer = n * 12000 + 2000 * (k - n/10);
        }
        return answer;
    }
}