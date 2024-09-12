import com.ibm.as400.access.AS400;
import com.ibm.as400.access.CommandCall;

public class App1 {
    public static void main(String[] args) {
        AS400 system = new AS400("your_ibm_i_host", "your_username", "your_password");
        
        try {
            System.out.println("成功連線到 IBM i");
            
            CommandCall command = new CommandCall(system, "DSPLIBL");
            if (command.run()) {
                System.out.println("命令執行結果: " + command.getMessageList());
            } else {
                System.err.println("命令執行失敗: " + command.getMessageList());
            }
        } catch (Exception e) {
            System.err.println("連線失敗: " + e.getMessage());
        } finally {
            if (system != null) {
                system.disconnectAllServices();
                System.out.println("已成功關閉連線");
            }
        }
    }
}
