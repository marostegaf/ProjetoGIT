public class Equals {
    public static void main(String[] args) {
        String n1 = "Curso";
        String n2 = "Video";
        String n3 = n1 + n2;
        String n4 = "CursoVideo";

        System.out.println(n3 == n4);
        System.out.println(n3.equals(n4));

    }
}
