import java.util.Scanner;
import java.lang.Math;

public class SuperCalculadora {
    public static void main(String[] args) {
        Scanner info = new Scanner(System.in);
        
        System.out.print("Digite um valor: ");
        int val = info.nextInt();
        int resto_divisao = val % val;
        double elevado_ao_cubo = Math.pow(val, 3);
        double raiz_quadrada = Math.sqrt(val);
        double raiz_cubica = Math.cbrt(val);
        int val_absoluto = Math.abs(val);
        
        System.out.println(" ");
        System.out.println("Resto da Divisão: " + resto_divisao);
        System.out.printf("Elevado ao Cubo: %.2f\n",elevado_ao_cubo);
        System.out.printf("Raiz Quadrada: %.2f\n", raiz_quadrada);
        System.out.printf("Raiz Cubica: %.2f\n", raiz_cubica);
        System.out.println("Valor Absoluto: " + val_absoluto);
    }   
}

