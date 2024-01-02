using IBM.Data.DB2.Core;

namespace MyApp
{
    public class Program
    {
        static void Main()
        {
            // 設定連線資訊
            var connectString = "Database=TSDDSCOS; UID=ibmecs; PWD=ibmecsusr; Server=TSDDSCOS";
            DB2Connection cn = new(connectString);
            // 開啟連線
            cn.Open();
            // 測試連線
            DB2Command cmd = new("SELECT * FROM QSYS2.ASP_INFO", cn);

            // 執行查詢
            try
            {
                var rtn = cmd.ExecuteReader();
                // 顯示資料
                while (rtn.Read())
                {
                    Console.WriteLine("{0} {1}", rtn["ASP_NUMBER"], rtn["ASP_STATE"]);
                }
            }
            finally
            {
                // 關閉連線
                cn.Close();
            }
        }
    }

}