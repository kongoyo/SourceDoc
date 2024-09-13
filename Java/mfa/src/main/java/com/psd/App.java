package com.psd;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import com.ibm.as400.access.AS400;
import com.ibm.as400.access.AS400SecurityException;
import com.ibm.as400.access.ConnectionDroppedException;
import com.warrenstrange.googleauth.GoogleAuthenticator;
import com.warrenstrange.googleauth.GoogleAuthenticatorKey;
import java.io.IOException;

/**
 * Hello world!
 */
public final class App {
    private App() {
    }

    /**
     * Says hello to the world.
     * @param args The arguments of the program.
     */
    public static void main(String[] args) {
        JFrame frame = new JFrame("IBM i 登錄");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);
        frame.setLayout(new GridBagLayout());  // 改用 GridBagLayout 以更好地控制佈局

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.insets = new Insets(5, 5, 5, 5);  // 添加一些內邊距

        JTextField ipField = new JTextField();
        JTextField userField = new JTextField();
        JPasswordField passwordField = new JPasswordField();
        JButton loginButton = new JButton("登錄");

        // 設置輸入框的首選大小
        Dimension fieldSize = new Dimension(150, 25);
        ipField.setPreferredSize(fieldSize);
        userField.setPreferredSize(fieldSize);
        passwordField.setPreferredSize(fieldSize);

        // 添加組件到框架
        gbc.gridx = 0;
        gbc.gridy = 0;
        frame.add(new JLabel("IP 地址:"), gbc);

        gbc.gridx = 1;
        frame.add(ipField, gbc);

        gbc.gridx = 0;
        gbc.gridy = 1;
        frame.add(new JLabel("用戶名:"), gbc);

        gbc.gridx = 1;
        frame.add(userField, gbc);

        gbc.gridx = 0;
        gbc.gridy = 2;
        frame.add(new JLabel("密碼:"), gbc);

        gbc.gridx = 1;
        frame.add(passwordField, gbc);

        gbc.gridx = 1;
        gbc.gridy = 3;
        frame.add(loginButton, gbc);

        JTextField mfaCodeField = new JTextField();
        JButton setupMFAButton = new JButton("設置 MFA");
        JButton useBackupCodeButton = new JButton("使用備用碼");

        // 添加新的 UI 元素
        gbc.gridx = 0;
        gbc.gridy = 3;
        frame.add(new JLabel("MFA 代碼:"), gbc);

        gbc.gridx = 1;
        frame.add(mfaCodeField, gbc);

        gbc.gridx = 0;
        gbc.gridy = 4;
        frame.add(setupMFAButton, gbc);

        gbc.gridx = 1;
        frame.add(useBackupCodeButton, gbc);

        gbc.gridx = 1;
        gbc.gridy = 5;
        frame.add(loginButton, gbc);

        // 設置 MFA 按鈕事件
        setupMFAButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                setupMFA();
            }
        });

        // 使用備用碼按鈕事件
        useBackupCodeButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                useBackupCode();
            }
        });

        // 修改登錄按鈕事件
        loginButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String ip = ipField.getText();
                String user = userField.getText();
                String password = new String(passwordField.getPassword());
                
                try {
                    AS400 system = new AS400(ip, user, password);
                    system.connectService(AS400.COMMAND);
                    JOptionPane.showMessageDialog(frame, "登錄成功！", "成功", JOptionPane.INFORMATION_MESSAGE);
                    system.disconnectAllServices();
                } catch (AS400SecurityException ex) {
                    JOptionPane.showMessageDialog(frame, "登錄失敗：認證錯誤", "錯誤", JOptionPane.ERROR_MESSAGE);
                } catch (ConnectionDroppedException ex) {
                    JOptionPane.showMessageDialog(frame, "登錄失敗：連接中斷 - " + ex.getMessage(), "錯誤", JOptionPane.ERROR_MESSAGE);
                } catch (IOException ex) {
                    JOptionPane.showMessageDialog(frame, "登錄失敗：IO錯誤 - " + ex.getMessage(), "錯誤", JOptionPane.ERROR_MESSAGE);
                } catch (Exception ex) {
                    JOptionPane.showMessageDialog(frame, "登錄失敗：" + ex.getMessage(), "錯誤", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        frame.pack();  // 自動調整框架大小以適應內容
        frame.setVisible(true);
    }

    private static void setupMFA() {
        GoogleAuthenticator gAuth = new GoogleAuthenticator();
        final GoogleAuthenticatorKey key = gAuth.createCredentials();
        
        String secretKey = key.getKey();
        // 在這裡，您應該將 secretKey 安全地存儲到用戶的帳戶中
        
        JOptionPane.showMessageDialog(null, "您的 MFA 密鑰是: " + secretKey + "\n請將此密鑰輸入到您的 Google Authenticator 應用中。", "MFA 設置", JOptionPane.INFORMATION_MESSAGE);
    }

    private static void verifyMFA(JTextField mfaCodeField) {
        String mfaCode = mfaCodeField.getText();
        GoogleAuthenticator gAuth = new GoogleAuthenticator();
        
        // 從用戶帳戶中檢索 secretKey
        String secretKey = retrieveSecretKeyFromUserAccount();
        
        boolean isCodeValid = gAuth.authorize(secretKey, Integer.parseInt(mfaCode));
        
        if (isCodeValid) {
            JOptionPane.showMessageDialog(null, "MFA 驗證成功！", "成功", JOptionPane.INFORMATION_MESSAGE);
        } else {
            JOptionPane.showMessageDialog(null, "MFA 驗證失敗！", "錯誤", JOptionPane.ERROR_MESSAGE);
        }
    }

    private static void useBackupCode() {
        String backupCode = JOptionPane.showInputDialog(null, "請輸入備用驗證碼：", "使用備用碼", JOptionPane.QUESTION_MESSAGE);
        // 在這裡實現備用碼驗證邏輯
        // 您需要事先生成並安全存儲一些備用碼
    }

    private static String retrieveSecretKeyFromUserAccount() {
        // 實現從用戶帳戶檢索 secretKey 的邏輯
        return "dummySecretKey";
    }
}
