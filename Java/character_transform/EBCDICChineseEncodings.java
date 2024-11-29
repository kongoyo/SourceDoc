import java.nio.charset.Charset;
import java.util.SortedMap;

public class EBCDICChineseEncodings {
    public static void main(String[] args) {
        // 獲取所有可用的字符集
        SortedMap<String, Charset> charsets = Charset.availableCharsets();
        
        System.out.println("IBM i EBCDIC 繁體中文相關編碼：");
        System.out.println("================================");
        
        // 遍歷並篩選出 EBCDIC 相關的繁體中文編碼
        for (String name : charsets.keySet()) {
            if (isEBCDICChineseTraditional(name)) {
                Charset charset = charsets.get(name);
                System.out.println("編碼名稱: " + name);
                System.out.println("顯示名稱: " + charset.displayName());
                System.out.println("別名: " + charset.aliases());
                System.out.println("--------------------------------");
            }
        }
    }
    
    private static boolean isEBCDICChineseTraditional(String charsetName) {
        charsetName = charsetName.toLowerCase();
        return (charsetName.contains("ebcdic") && 
                (charsetName.contains("traditional") || 
                 charsetName.contains("taiwan") || 
                 charsetName.contains("big5") || 
                 charsetName.contains("cp937") ||
                 charsetName.contains("cp835") ||
                 charsetName.contains("cp1371")));
    }
} 