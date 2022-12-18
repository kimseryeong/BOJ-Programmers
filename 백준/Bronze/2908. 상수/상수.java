import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String input = br.readLine();
		
		//입력값 뒤집기 
		StringBuffer sb = new StringBuffer(input);
		String reverse = sb.reverse().toString();
		
		//공백을 기준으로 숫자 나누기 
		StringTokenizer st;
		st = new StringTokenizer(reverse, " ");
		
		int num1 = Integer.parseInt(st.nextToken());
		int num2 = Integer.parseInt(st.nextToken());
		
		//두 수 비교 
		if(num1 > num2) {
			System.out.println(num1);
		}else {
			System.out.println(num2);
		}
		
	}

}
