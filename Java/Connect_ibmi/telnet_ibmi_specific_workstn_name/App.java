
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;


public class App {
    public static void main(String[] args) throws Exception {
        try {
            String IBM_I_HOST = "172.16.14.61"; // Replace with the actual IBM i host IP address
            int IBM_I_PORT = 23; // Replace with the actual IBM i port number
            String AS400_USER = "QSECOFR"; // Replace with the actual IBM i user ID
            String AS400_PASSWORD = "password"; // Replace with the actual IBM i password
            int STARTING_DIGIT = 0; // Replace with the starting digit for the workstation IDs
            int ENDING_DIGIT = 99; // Replace with the ending digit for the workstation IDs

            String DRIVER = "com.ibm.as400.access.AS400JDBCDriver";
            String URL = "jdbc:as400://172.16.13.34";

            System.out.println("Trying to connect...");

            Class.forName(DRIVER);
            Connection conn = DriverManager.getConnection(URL,AS400_USER,AS400_PASSWORD );
                // Execute TELNET login for each workstation
                for (int i = STARTING_DIGIT; i <= ENDING_DIGIT; i++) {
                    String workstationID = "BATMAN" + String.format("%02d", i);
                    try {
                        Statement stmt = conn.createStatement();

                        // Check for successful TELNET login
                        ResultSet rs = stmt.executeQuery("select * from sysibm.sysdummy1");
                        if (rs.next() && rs.getString("IBMREQD").equals("Y")) {
                            System.out.println("Successful login with workstation ID: " + workstationID);
                        } else {
                            System.err.println("Failed to login with workstation ID: " + workstationID);
                        }
                        rs.close();
                        stmt.close();
                    } catch (SQLException e) {
                        System.err.println("Error executing SIGNON command for workstation ID: " + workstationID);
                        e.printStackTrace();
                    }
                }    
                conn.close();
                System.exit(0);
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            } catch (SQLException e) {
                e.printStackTrace();
            }
    }
}
