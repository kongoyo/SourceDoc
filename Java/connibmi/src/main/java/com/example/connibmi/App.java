package com.example.connibmi;

import java.io.IOException;
import java.util.Enumeration;

import com.ibm.as400.access.AS400;
import com.ibm.as400.access.AS400SecurityException;
import com.ibm.as400.access.ErrorCompletingRequestException;
import com.ibm.as400.access.Job;
import com.ibm.as400.access.JobLog;
import com.ibm.as400.access.ObjectDoesNotExistException;
import com.ibm.as400.access.QueuedMessage;

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
            AS400 system = new AS400("172.16.13.58", "qsecofr", "password");
            
            // 獲取當前工作
            Job job = new Job(system);
            
            // 獲取工作日誌
            JobLog jobLog = job.getJobLog();
            
            System.out.println("工作日誌內容：");
            System.out.println("--------------------");
            
            // 遍歷工作日誌中的所有消息
            Enumeration<?> messageEnum = jobLog.getMessages();
            while (messageEnum.hasMoreElements()) {
                QueuedMessage message = (QueuedMessage) messageEnum.nextElement();
                // System.out.println("時間: " + message.getDate());
                System.out.println("類型: " + message.getType());
                System.out.println("嚴重性: " + message.getSeverity());
                System.out.println("消息: " + message.getText());
                System.out.println("--------------------");
            }
            
            // 斷開連接
            system.disconnectAllServices();
        } catch (IOException | AS400SecurityException | ObjectDoesNotExistException | ErrorCompletingRequestException | InterruptedException e) {
            System.err.println("錯誤: " + e.getClass().getSimpleName() + " - " + e.getMessage());
            // 可以考慮使用日誌框架，如 log4j 或 java.util.logging
            // Logger.getLogger(App.class.getName()).log(Level.SEVERE, "發生錯誤", e);
        }
    }
}
