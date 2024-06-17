import java.sql.*;

public class ibmiconn_customers {
    public static void main(String[] args) throws Exception {
        try {
            System.out.println("Trying to connect...");
            String driver = "com.ibm.as400.access.AS400JDBCDriver";
            String url = "jdbc:as400://172.16.14.61";
            Class.forName(driver);
            Connection conn = DriverManager.getConnection(url, "QSECOFR", "PASSWORD");
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("select * from ddscinfo.customers limit 5");
            System.out.println("Connected with " + conn);
            // System.out.println("employee_code, employee_name, monthly_salary");
            while (rs.next()) {
                System.out.println(rs.getString("CUSTOMER_ID") + " " + rs.getString("FIRST_NAME") + " "
                        + rs.getString("LAST_NAME") + " " + rs.getString("EMAIL"));
            }
            conn.close();
            System.exit(0);
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
