import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int C = Integer.parseInt(br.readLine()); // 테스트 케이스 
		
		StringTokenizer st;
		int[] score;
		 
		for(int i = 0; i < C; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			
			int N = Integer.parseInt(st.nextToken()); // 학생의 수
			score = new int[N]; // N명의 점수 

			int sum = 0;
			
			// 점수 입력 
			for(int j = 0; j < score.length; j++) {
				score[j] = Integer.parseInt(st.nextToken());
				sum += score[j];
			}
			
			double avg = sum/N;
			double cnt = 0;
			
			for(int k = 0; k < N; k++) {
				if(score[k] > avg) {
					cnt++;
				}
			}
			System.out.printf("%.3f%%\n", (cnt/N*100));
		}
		
		
		
	}

}
