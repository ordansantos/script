import java.util.Scanner;

public class subconjunto {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int n = input.nextInt();
    int minOdd = 100000000;
    long ans = 0;
    while (n-- > 0) {
      int a = input.nextInt();
      ans += a;
      if (a % 2 != 0 && a < minOdd) {
        minOdd = a;
      }
    }
    if (ans % 2 != 0) {
      ans -= minOdd;
    }
    System.out.println(ans);
  }
}
