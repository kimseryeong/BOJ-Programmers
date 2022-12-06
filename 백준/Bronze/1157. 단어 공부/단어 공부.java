import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str = br.readLine().toUpperCase();
		
		// 총 알파벳 개수 담을 배열.. 
		int[] alpha = new int[26];
		
		// 입력된 문자열 길이만큼 반복하면서 해당 알파벳 개수 담기
		// ex) A기준으로 
		//     --> 'A' == 65 -> 'A'-65 == 0으로 배열 0번째(A) 값 증가
		for(int i = 0; i < str.length(); i++) {
			int order = str.charAt(i) - 65;
			alpha[order]++;
		}
		
		// 중복된다면 ? 반환, 중복되지 않으면 count 반환 
		char result = '?';
		int count = 0;
		
		for(int i = 0; i < alpha.length; i++) {
			if(count < alpha[i]) {
				count = alpha[i];
				result = (char)(i+'A');
			}else if(count == alpha[i]) {
				result = '?';
			}
		}
		System.out.println(result);
	}

}
