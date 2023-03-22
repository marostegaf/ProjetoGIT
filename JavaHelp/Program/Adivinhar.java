import java.util.Scanner;
import java.lang.Math;

public class Adivinhar {
    public static void main(String[] args) {
        double aleatorio = Math.random();
        int n = (int) (1 + aleatorio * (6 - 1));
        //double aleatorio = 1 + Math.random() * (6 - 1);
        //int n = (int) aleatorio;

        //Random r = new Random();
        //int numSorteado = 1 + r.nextInt(5);
        
        Scanner info = new Scanner(System.in);
        System.out.println("Tente adivinhar o número aleatório");
        System.out.print("Num: ");
        int num = info.nextInt();
        System.out.print("O número aleatório era [ " + n + " ] e você: ");
        String resposta = (num == n)?"Acertou":"Errou"; //"Acertou" + (variável)
        System.out.println(resposta);

    }
}
