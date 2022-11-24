import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		double[] arr = new double[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		double max = arr[0];
		double score = 0;
		
		// 시험점수 배열에 담기 
		for(int i = 0; i < arr.length; i++) {
			arr[i] = Double.parseDouble(st.nextToken());
		}
		// 최고점 찾기 
		for(int i = 0; i < arr.length; i++) {
			if(max < arr[i]) {
				max = arr[i];
			}
		}
		
		// 시험 점수 계산하기 
		for(int i = 0; i < N; i++) {
			score += ((arr[i] / max) * 100);
		}
		System.out.println(score / arr.length);
	}

}
