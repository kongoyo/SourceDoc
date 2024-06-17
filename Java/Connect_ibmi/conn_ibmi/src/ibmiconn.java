import java.sql.*;

public class ibmiconn {
    public static void main(String[] args) throws Exception {
        try {
            System.out.println("Trying to connect...");
            String DRIVER = "com.ibm.as400.access.AS400JDBCDriver";
            String URL = "jdbc:as400://172.16.14.61";
            Class.forName(DRIVER);
            Connection conn = DriverManager.getConnection(URL, "QSECOFR", "PASSWORD");
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(
                    "select AMBSYSN, AMBLIB, AMBFILE, AMBNAME, AMBNRCD, BMBSYSN, BMBLIB, BMBFILE, BMBNAME, BMBNRCD from DDSCINFO.CMPPFMBR");
            System.out.println("Connected with " + conn);
            // System.out.println("employee_code, employee_name, monthly_salary");
            while (rs.next()) {
                if (rs.getString("BMBSYSN") != null || rs.getString("BMBLIB") != null
                        || rs.getString("BMBFILE") != null) {
                    System.out.println(rs.getString("AMBSYSN") + " " + rs.getString("AMBLIB") + " " + rs.getString("AMBFILE") + " "
                            + rs.getString("BMBSYSN") + " " + rs.getString("BMBLIB") + " " + rs.getString("BMBFILE"));
                }
            }
            conn.close();
            System.exit(0);
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
