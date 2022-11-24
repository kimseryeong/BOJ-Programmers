import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		String[] str = new String[N];
		
		for(int i = 0; i < N; i++) {
			str[i] = br.readLine();
		}
		
		for(int i = 0; i < N; i++) {
			int cnt = 0;
			int sum = 0;
			
			// OX string -> char 변환 
			for(int j = 0; j < str[i].length(); j++) {
				if(str[i].charAt(j) == 'O') {
					cnt++;
				}else {
					cnt = 0; // X가 나오면 cnt 초기화 
				}
				sum += cnt;
			}
			System.out.println(sum);
		}
	}

}
