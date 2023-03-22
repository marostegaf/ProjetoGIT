import java.util.Scanner;

public class MathJ {
    public static void main(String[] args) {

        int numero = 10;
        int valor = 4 + --numero;
        System.out.println(valor);
        System.out.println(numero);
        
        
        float v = 8.5f;

        int ar = (int) Math.floor(v); // Para baixo
        int ar1 = (int) Math.ceil(v); // Para cima
        int ar2 = (int) Math.round(v); // Valor aritimético
        System.out.println(v + " " + ar + " " + ar1 + " " + ar2);
        

        
        double aleatorio = Math.random();
        int num = (int) (1 + aleatorio * (100 - 1));
        System.out.println(num);
        
        
        
        Scanner info = new Scanner(System.in);
        
        System.out.print("Num: ");
        float n = info.nextFloat();
        float raiz = (float) Math.sqrt(n); // NUMERO QUE DIVIDINDO POR ELE MESMO = RAIZ
        int exponenciacao = (int) Math.pow(n, n); // NUM X NUM = EXPONENCIAÇÃO
        float raizCubica = (float) Math.cbrt(n); // NUM X ((NUM) PELA QUANTIDADE QUE FOI ELEVADO) = RAIZ CUBICA
        System.out.printf("Raiz de %.0f = %.2f\n", n, raiz);
        System.out.println(exponenciacao);
        System.out.println(raizCubica); // CUBICA DE 27 = 3 POIS 3 X 3 X 3 = 27
        
        info.close();
    }   
}
