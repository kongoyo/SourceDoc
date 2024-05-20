import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class ContactManager {
    private Map<String, String> contacts = new HashMap<>();

    public void addContact(String name, String phone) {
        contacts.put(name, phone);
    }

    public String getContact(String name) {
        return contacts.get(name);
    }

    public void updateContact(String name, String newPhone) {
        if (contacts.containsKey(name)) {
            contacts.put(name, newPhone);
        } else {
            System.out.println("聯絡人不存在。");
        }
    }

    public void deleteContact(String name) {
        if (contacts.containsKey(name)) {
            contacts.remove(name);
        } else {
            System.out.println("聯絡人不存在。");
        }
    }

    public static void main(String[] args) {
        ContactManager manager = new ContactManager();
        Scanner scanner = new Scanner(System.in);
        String name, phone;

        while (true) {
            System.out.println("通訊錄管理系統");
            System.out.println("1. 新增聯絡人");
            System.out.println("2. 查詢聯絡人");
            System.out.println("3. 更新聯絡人");
            System.out.println("4. 刪除聯絡人");
            System.out.println("5. 退出");
            System.out.print("請選擇操作：");

            int choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    System.out.print("輸入姓名：");
                    name = scanner.next();
                    System.out.print("輸入電話：");
                    phone = scanner.next();
                    manager.addContact(name, phone);
                    break;
                case 2:
                    System.out.print("輸入姓名：");
                    name = scanner.next();
                    phone = manager.getContact(name);
                    System.out.println("電話號碼：" + phone);
                    break;
                case 3:
                    System.out.print("輸入姓名：");
                    name = scanner.next();
                    System.out.print("輸入新電話：");
                    phone = scanner.next();
                    manager.updateContact(name, phone);
                    break;
                case 4:
                    System.out.print("輸入姓名：");
                    name = scanner.next();
                    manager.deleteContact(name);
                    break;
                case 5:
                    System.out.println("退出系統。");
                    scanner.close();
                    return;
                default:
                    System.out.println("無效的操作。");
                    break;
            }
        }
    }
}
