import java.util.Scanner;

public class Pernas {
    public static void main(String[] args) {
        Scanner info = new Scanner(System.in);
        
        System.out.print("Quantas Pernas: ");
        int pernas = info.nextInt();

        String tipo;
        switch (pernas) {
            case 1: 
                tipo = "Saci";
                break;
            case 2:
                tipo = "Bípede";
                break;
            case 3:
                tipo = "Tripé";
                break;
            case 4:
                tipo = "Quadrúpede";
                break;
            case 6:case 8:
                tipo = "Aranha";
                break;
            default: 
                tipo = "ET";
        }
        System.out.println(tipo);       
    }
}

