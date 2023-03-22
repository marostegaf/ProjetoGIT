import java.util.Scanner;
import java.lang.Math;

public class Bask {
    public static void main(String[] args) {
        Scanner info = new Scanner(System.in);

        System.out.print("A: " );
        int a = info.nextInt();
        System.out.print("B: ");
        int b = info.nextInt();
        System.out.print("C: " );
        int c = info.nextInt();
        
        //                Math.pow(b, 2) = b * b
        double bhaskara = Math.pow(b, 2) - 4 * (a * c);
        System.out.printf("Delta: %.2f\n", bhaskara);

        System.out.print("Tipo: ");
        if (bhaskara >= 0) {
            System.out.print("Existem raízes reais!");
        } else {
            System.out.println("Não existem raízes reais!");
        }
    }
}

