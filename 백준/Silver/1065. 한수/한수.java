import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int result = hansu(sc.nextInt());
		
		System.out.println(result);
		
	}
	public static int hansu(int n) {
		int cnt = 0;
		
		// 100보다 작은 수는 모두 한수 
		if(n < 100) {
			return n; // 자기자신 == 한수의 개수 
		}
		
		// 100 이상
		else {
			cnt = 99;
			
			for(int i = 100; i <= n; i++) {
				// 백의자리, 십의자리, 일의자리 
				int hundred = i / 100;
				int ten = (i / 10) % 10;
				int one = i % 10;
				
				// 수열 확인 
				if( (hundred - ten) == (ten - one) ) {
					cnt++;
				}
			}
		}

		return cnt;
	}
}
