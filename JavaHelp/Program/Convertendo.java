public class Convertendo {
    public static void main(String[] args) {
        int idade = 30;
        String valor = Integer.toString(idade);
        System.out.println(valor);

        String valor1 = "30";
        int idade1 = Integer.parseInt(valor1);
        System.out.println(idade1);

        String valor2 = "30";
        float idade2 = Float.parseFloat(valor2);
        System.out.printf("%.3f \n", idade2);
        
        int valor3 = 30;
        String idade3 = Integer.toString(valor3);
        System.out.println(idade3);

    }
}
