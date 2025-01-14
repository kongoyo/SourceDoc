const odbc = require('odbc');

// 連接設定
const connectionConfig = {
    connectionString: 'DSN=clark75_13_58;SYSTEM=172.16.13.58;UID=ibmecs;PWD=ibmecsusr;NAMING=1;LIBRARY=DDSCINFO',
    connectionTimeout: 10,
    loginTimeout: 10
};

async function connectToDb2() {
    try {
        // 建立連接
        const connection = await odbc.connect(connectionConfig);
        console.log('成功連接到 DB2 for IBM i');

        // 測試查詢
        const result = await connection.query('SELECT * FROM DDSCINFO.EMAIL LIMIT 5');
        console.log('查詢結果:', result);

        // 測試新增
        const insertQuery = "INSERT INTO DDSCINFO.EMAIL (TEAM, EMAILADDR) VALUES ('TEST01', 'test01@example.com')";
        const insertResult = await connection.query(insertQuery);
        console.log('新增結果:', insertResult);

        // 測試修改
        const updateQuery = "UPDATE DDSCINFO.EMAIL SET EMAILADDR = 'TESTUP@example.com' WHERE TEAM = 'TEST01'";
        const updateResult = await connection.query(updateQuery);
        console.log('修改結果:', updateResult);

        // 測試刪除
        const deleteQuery = "DELETE FROM DDSCINFO.EMAIL WHERE TEAM = 'TEST01'";
        const deleteResult = await connection.query(deleteQuery);
        console.log('刪除結果:', deleteResult);

        // 關閉連接
        await connection.close();
        console.log('連接已關閉');

    } catch (error) {
        console.error('連接錯誤:', error);
    }
}

// 執行連接函數
connectToDb2();