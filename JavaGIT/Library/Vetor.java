import java.util.Arrays;

import javax.swing.DefaultListModel;

public class Vetor {
    public static void main(String[] args) {
        int n[] = new int[4];

        System.out.println(n);
        System.out.println(" ");

        for (int valor : n) {
            System.out.print(valor + " ");
        }
        System.out.println(" ");

        int n1[] = { 3, 2, 8, 7, 5, 4 };
        for (int c = 0; c <= n1.length - 1; c++) {
            System.out.print(n1[c] + " ");
        }
        System.out.println(" ");

        DefaultListModel lista = new DefaultListModel<>();
        System.out.println(lista);
        // Aprende usar esse metodo no programa "DefaultList"

    }
}
