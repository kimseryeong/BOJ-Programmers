public class Main {
	public static void main(String[] args) {
		// 셀프넘버 여부 확인 
		boolean[] b = new boolean[10001];
		
		for(int i = 1; i <= 10000; i++) {
			int n = d(i);
			
			if(n <= 10000) {
				b[n] = true;
			}
		}
		for(int i = 1; i <= 10000; i++) {
			if(b[i] == false) {
				System.out.println(i);
			}
		}
	}
	
	// 함수 생성 
	public static int d(int num) {
		// num : sum의 생성자 ??
		int sum = num;
		
		while(num != 0) {
			sum += num % 10; // 각 자리 수 더하기 
			num = num / 10; // 일의자리 수 없애기 
		}
		return sum;
	}
}
