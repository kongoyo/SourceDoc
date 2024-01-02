using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using IBM.Data.IbmI;

namespace Login
{
    public class Program
    {
        public static void Main(string[] args)
        {
            // 設定連線資訊
            var connectionInfo = new IBMiConnectionInfo
            {
                Host = "192.168.1.100",
                Port = 446,
                UserId = "user",
                Password = "password",
                Database = "database",
            };

            // 建立連線
            var connection = new IBMiConnection(connectionInfo);

            // 測試連線
            if (connection.IsConnected)
            {
                Console.WriteLine("連線成功");

                // 查詢資料
                var customers = connection.Query("SELECT * FROM CUSTOMERS");

                // 顯示資料
                foreach (var customer in customers)
                {
                    Console.WriteLine("{0} {1}", customer.CustomerId, customer.Name);
                }
            }
            else
            {
                Console.WriteLine("連線失敗");
            }

            // 關閉連線
            connection.Close();
        }
    }
}
