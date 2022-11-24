import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int [] arr = new int[10];
		int cnt = 0; // 최종 개수 세기 
		int temp; 
		
		for(int i = 0; i < 10; i++) {
			arr[i] = Integer.parseInt(br.readLine())%42;
		}
		
		// 두 값 비교하면서 찾기
		for(int i = 0; i < arr.length; i++) {
			temp = 0;
			for(int j = i+1; j < arr.length; j++) {
				// 나머지가 서로 같으면 temp 값++
				if(arr[i] == arr[j]) {
					temp ++;
				}
			}
			// temp == 0이면 서로 다른 나머지임 
			if(temp == 0) {
				cnt++;
			}
		}
		System.out.println(cnt);
	}
	

}
