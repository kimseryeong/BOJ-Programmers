import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
//		WXYZ -> 9 -> +10
//		TUV -> 8 -> +9
//		PQRS -> 7 -> +8
//		MNO -> 6 -> +7
//		JKL -> 5 -> +6
//		GHI -> 4 -> +5
//		DEF -> 3 -> +4
//		ABC -> 2 -> +3
		
		// 알파벳 배열에 다이얼 숫자 넣어놓기?
		int[] alpha = new int[26];
		for(int i = 0; i < 3; i++){
			alpha[i] = 3;
		}
		for(int i = 3; i < 6; i++){
			alpha[i] = 4;
		}
		for(int i = 6; i < 9; i++) {
			alpha[i] = 5;
		}
		for(int i = 9; i < 12; i++){
			alpha[i] = 6;
		}
		for(int i = 12; i < 15; i++){
			alpha[i] = 7;
		}
		for(int i = 15; i < 19; i++) {
			alpha[i] = 8;
		}
		for(int i = 19; i < 22; i++) {
			alpha[i] = 9;
		}
		for(int i = 22; i < 26; i++) {
			alpha[i] = 10;
		}
		
		String input = br.readLine();
		char[] dial= {};
		
		int sum = 0;
		
		for(int i = 0 ; i < input.length(); i++) {
			char c1 = input.charAt(i);
			//System.out.println(c1);
			sum += alpha[c1-'A'];
		}
		System.out.println(sum);
		
		
		
	}

}
