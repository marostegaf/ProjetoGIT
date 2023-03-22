import java.util.Calendar;

public class Ano {
    public static void main(String[] args) {
        Calendar cal = Calendar.getInstance();
        int ano = cal.get(Calendar.YEAR);
        System.out.println(ano);
    }
}
