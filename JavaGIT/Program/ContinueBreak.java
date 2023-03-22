public class ContinueBreak {
    public static void main(String[] args) {
        int cc = 0;
        int cc2 = 0;
        while (cc < 10) {
            cc++;
            if (cc == 2 || cc == 4 || cc == 5) {
                continue; // Interrupo o fluxo natural e ignora o restante do código
            }
            System.out.println("Cambalhota: " + cc);

        }

        while (cc2 < 10) {
            cc2++;
            if (cc2 == 5) {
                break;
            }
            System.out.println("Cambalhota 2: " + cc2);
        }
    }
}
