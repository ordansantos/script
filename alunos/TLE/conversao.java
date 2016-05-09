import java.util.Scanner;

public class conversao {
  public static void main(String[] args) {
	int k = 1;
	  while (k != 1000000000) k++;
    Scanner input = new Scanner(System.in);
    int n = input.nextInt();
    System.out.println(n * 50);
  }
}
