import java.util.*;
class Solution {
    public int solution(int[][] dots) {
        int answer = 0;
        float grade [] = new float[6]; // 직선 6개의 기울기 담은 배열
        int index = 0; // 기울기 배열 index
        
        // 두 직선이 평행 == 두 직선의 기울기가 같음
        // 4개의 점으로 총 6개의 직선(기울기) 생김
        for(int i = 0; i < 3; i++){
            for(int j = i+1; j < 4; j++){
                float result = (float)(dots[i][1]-dots[j][1])
                    /(float)(dots[i][0]-dots[j][0]); // 기울기
                
                grade[index] = result;
                index++;
            }
        }
        
        // 평행 여부 확인
        for(int i = 0; i < grade.length-1; i++){
            for(int j = i+1; j < grade.length; j++){
                if(grade[i] == grade[j]){
                    return 1;
                }
            }
        }
        
        return answer;
    }
}