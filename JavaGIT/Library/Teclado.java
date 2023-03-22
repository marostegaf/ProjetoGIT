import java.util.Scanner;

public class Teclado {
    public static void main(String[] args) {
        Scanner info = new Scanner(System.in);
        
        System.out.print("Num: ");
        int num = info.nextInt();

        System.out.print("\nString: ");
        String string = info.nextLine();

        System.out.println("Número digitado: " + num + "String digitada: " + string);
    }
}
