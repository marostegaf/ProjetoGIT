//import java.util.*;
import java.util.Locale;

public class idioma {
    public static void main(String[] args) {
        Locale idioma = Locale.getDefault();
        System.out.print("O idioma do seu sistema está configurado para: " +idioma.getDisplayLanguage());
        //System.out.println(idioma.getDisplayLanguage());
    }
}
