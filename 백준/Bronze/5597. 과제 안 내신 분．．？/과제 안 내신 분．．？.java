import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		boolean [] arr = new boolean[31];
		
		// 과제를 제출한 28명의 출석번호는 true로 저장!
		for(int i = 0; i < 28; i++) {
			int student = sc.nextInt(); //출석번호 
			arr[student] = true;
		}
		for(int i = 1; i < arr.length; i++) {
			// 과제를 제출하지 않은 2명의 출석번호 false로 저장 !
			if(!arr[i]) {
				System.out.println(i);
			}
		}
	}

}
