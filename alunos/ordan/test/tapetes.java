

import java.util.Scanner;

public class tapete {
	public static void main (String[] args){
		Scanner sc = new Scanner(System.in);
		long L = sc.nextInt();
		long N = sc.nextInt();
		System.out.println ((L-N+1)*(L-N+1) + N - 1);
	} 
}
