import com.ibm.AS400;

public class App {
    public static void main(String[] args) throws Exception {
        String systemip = "172.16.14.61";
        String userid = "QSECOFR";
        char[] userpw = {'P', 'A', 'S', 'S', 'W', 'O', 'R', 'D'};

        AS400 as400 = new AS400(systemip, userid, userpw);

        
        
        System.out.println("Hello, World!");
    }
}
