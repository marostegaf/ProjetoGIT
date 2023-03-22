import java.util.Scanner;
import javax.swing.DefaultListModel;

public class DefautList {
    public static void main(String[] args) {
        Scanner info = new Scanner(System.in);
        //Criando a lista usando DefaultListModel      
        DefaultListModel lista = new DefaultListModel<>();

        //Adicionando 5 valores na lista
        System.out.println("Digite 5 números para colocar na Lista: ");
        int c = 0;
        while (c <= 4) {
            int num = info.nextInt();
            lista.addElement(num);
            c++;
        }

        //Adicionando um número na lista
        System.out.print("Número para adicionar: ");
        int num_adicionar = info.nextInt();
        lista.addElement(num_adicionar);

        //Removendo o número escolhido da lista
        System.out.print("Número para remover: ");
        int num_remover = info.nextInt();
        lista.removeElement(num_remover);

        //Mostrando a lista
        System.out.println(lista);

        //Limpando a lista
        lista.clear();
        System.out.println(lista);
    
    }
}