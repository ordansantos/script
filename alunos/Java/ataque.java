import java.util.Scanner;

public class ataque {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int[] a = new int[4000];
    int[] b = new int[4000];
    int n = input.nextInt();
    for (int i = 0; i < n; i++) {
      int x = input.nextInt();
      int y = input.nextInt();
      a[x + y]++;
      b[x - y + 1000]++;
    }
    long ans = 0;
    for (int i = 0; i < a.length; i++) {
      ans += a[i] * (a[i] - 1) / 2;
      ans += b[i] * (b[i] - 1) / 2;
    }
    System.out.println(ans);
  }
}
