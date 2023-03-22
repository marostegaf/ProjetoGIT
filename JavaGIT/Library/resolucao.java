import java.awt.Dimension;
import java.awt.Toolkit;

public class resolucao {
    public static void main(String[] args) {
        Dimension size = Toolkit.getDefaultToolkit().getScreenSize();

        int largura = (int) size.getWidth();
        int altura = (int) size.getHeight();

        System.out.println("Sua resolução é de:"+ " " +largura+ " X " +altura); 
    }
}
/*
Outro jeito fazendo direto sem precisar criar uma variável para Altura e Tamanho:
System.out.println("Sua resolução é de:"+ " " +size.getHeight()+ " X " +size.getWidth()); 
System.out.println("Tamanho:"+(int)size.getWidth() + " " + (int)size.getHeight());

Sua resolução é de" (+" " para adicionar o espaço) (+largura+ para colocar a variável)
((" X ") para colocar o X na interface) e (+altura para adicionar a variável))
*/
