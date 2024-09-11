package com.example.connibmi;

import com.ibm.as400.access.AS400;
import com.ibm.as400.access.CommandCall;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        try {
            // 創建AS400對象,替換為您的IBM i系統地址、用戶名和密碼
            AS400 system = new AS400("172.16.13.34", "qsecofr", "password");
            
            // 執行一個簡單的命令來測試連接
            CommandCall cmd = new CommandCall(system, "DSPJOBLOG");
            if (cmd.run()) {
                System.out.println("成功連接到IBM i系統!");
            } else {
                System.out.println("連接失敗: " + cmd.getMessageList()[0].getText());
            }
            
            // 斷開連接
            system.disconnectAllServices();
        } catch (Exception e) {
            System.out.println("發生錯誤: " + e.getMessage());
        }
    }
}
