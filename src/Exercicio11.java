import java.util.Scanner;

public class Exercicio11 {
    public static void main(String[] args) {
    Scanner leitor=new Scanner(System.in);
    System.out.print("digiter o valor do produto : ");
    double produto=leitor.nextInt();
    produto=produto-(produto*0.10);
    System.out.println("o valor do produto :"+produto);
}
}
