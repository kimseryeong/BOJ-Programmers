import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		//split은 공백을 포함해서 개수를 세기 때문에
		//단어없이 공백만 있는 경우도 개수를 센다.
		//String[] word = str.split(" ");
		
		String str = br.readLine();
		StringTokenizer st = new StringTokenizer(str, " ");
		
		// StringTokenizer 개수 세기 -> countTokens() 
		System.out.println(st.countTokens());

	}

}
