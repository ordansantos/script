import java.util.Scanner;

public class erro {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    String string = input.next();
    for (int i = 1; i < string.length(); i++) {
      System.out.print(string.charAt(i));
    }
    System.out.println("");
  }
}
