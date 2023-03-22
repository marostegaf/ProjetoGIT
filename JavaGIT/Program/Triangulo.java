import java.util.Scanner;

public class Triangulo {
    public static void main(String[] args) {
        Scanner info = new Scanner(System.in);
        
        System.out.println("Forme um triângulo!");
        System.out.print("A: ");
        int a = info.nextInt();
        System.out.print("B: ");
        int b = info.nextInt();
        System.out.print("C: ");
        int c = info.nextInt();

        if (a < b + c && b < a + c && c < a + b){
            System.out.print("Esses segmentos formam um triângulo: ");
            if (a == b && b == c) { // Todos os lados iguais
                System.out.println("Equilátero");
            } else if (a != b && b != c && a != c) { // Nenhum lado igual
                System.out.println("Escaleno");
            } else { // 2 lados iguais
                System.out.println("Isósceles");
            }
        } else { 
            System.out.println("Esses segmentos não formam um triângulo!");
        }
        info.close();
    }
}

