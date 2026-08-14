import java.util.Scanner;

public class Exercico10 {
    public static void main(String[] args) {
        Scanner leitor=new Scanner(System.in);
        System.out.print("digite o seu nome :");
        String nome=leitor.nextLine();
        System.out.println("bom dia " + nome);
        leitor.close();
    }
}
