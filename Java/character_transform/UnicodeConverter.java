public class UnicodeConverter {
    public static void main(String[] args) {
        String input = "橰"; // 測試用的BIG5字元
        
        try {
            // 先將字串轉換成BIG5編碼的位元組
            byte[] big5Bytes = input.getBytes("Big5");
            
            // 輸出BIG5編碼的十六進位值
            System.out.println("BIG5編碼:");
            printBytes(big5Bytes);
            
            // 將BIG5位元組轉換回字串（使用Cp937 - Traditional Chinese EBCDIC）
            byte[] ebcdicBytes = new String(big5Bytes, "Big5")
                .getBytes("Cp937");
            
            // 輸出EBCDIC編碼的十六進位值
            System.out.println("\nEBCDIC編碼:");
            printBytes(ebcdicBytes);
            
        } catch (Exception e) {
            System.err.println("轉換過程發生錯誤: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    // 新增輔助方法來印出位元組陣列的內容
    private static void printBytes(byte[] bytes) {
        for (byte b : bytes) {
            System.out.printf("%02X ", b & 0xFF);
        }
        System.out.println(); // 換行
        
        // 同時顯示十進位值
        System.out.print("十進位: ");
        for (byte b : bytes) {
            System.out.printf("%d ", b & 0xFF);
        }
        System.out.println();
    }
}