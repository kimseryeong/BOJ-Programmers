import java.util.*;

class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        
        String[] origin = {"aya", "ye", "woo", "ma"};
        
        // 발음할 수 있는 경우 -> "공백"으로 만들어 버리고 count 세기!
        for(int i = 0; i < babbling.length; i++){
            for(String o : origin){
                babbling[i] = babbling[i].replace(o," ");
            }
            
            // babbling 배열이 공백인 경우 -> 발음 가능!!
            if(babbling[i].replaceAll(" ","").equals("")){answer ++;}
        }
        
        return answer;
    }
}