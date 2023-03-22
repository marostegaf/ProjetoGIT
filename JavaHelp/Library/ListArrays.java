import java.util.Arrays;

public class ListArrays {
    public static void main(String[] args) {
        int num[] = {3, 5, 1, 8, 4};
        
        //Mostra em que lugar está a variavel dentro da lista
        int pos = Arrays.binarySearch(num, 1);
        System.out.println("Posição do número 1: " + pos);

        //Mostra a lista
        System.out.print("Ordem normal: ");
        for (int valor: num) {
            System.out.print(valor + " ");
        }

        Arrays.sort(num); // Deixa a lista em ordem crescente 
        
        // Mostra a nova lista como ficou em ordem crescente
        System.out.print("\nOrdem crescente: ");
        for (int valor: num) {
            System.out.print(valor + " ");
        }
        
        //Preencher todos os valores com 0
        System.out.print("\nPreenchendo tudo com 0: ");
        int n[] = new int[5];
        Arrays.fill(n, 0);
        for (int valor: n) {
            System.out.print(valor + " ");
        }
    }
}
