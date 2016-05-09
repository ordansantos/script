import java.util.*;
public class ataque{
	public static void main(String [] args){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(), res = 0, mx[] = new int[3005], mn[] = new int[3005];
		for(int i = 1 ; i <= N ; i++){
			int x = sc.nextInt(), y = sc.nextInt();
			res += mx[x + y + 1000]++ + mn[x - y + 1000]++;
		}
		System.out.println(res);
	}
}
