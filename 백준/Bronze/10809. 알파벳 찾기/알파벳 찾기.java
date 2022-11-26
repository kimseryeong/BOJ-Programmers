import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		String s = sc.next();
		
		for(char c = 'a'; c <= 'z'; c++) {
			sb.append(s.indexOf(c) + " ");
		}
		System.out.println(sb);
	}

}
