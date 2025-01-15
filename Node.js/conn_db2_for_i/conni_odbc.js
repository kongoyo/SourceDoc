const odbc = require('odbc');

// 連接設定
const connectionConfig = {
    connectionString: 'DSN=clark75_13_58;SYSTEM=172.16.13.57;UID=ibmecs;PWD=ibmecsusr;NAMING=1;LIBRARY=DDSCINFO',
    connectionTimeout: 10,
    loginTimeout: 10
};

class Db2Connection {
    constructor(config) {
        this.config = config;
        this.connection = null;
    }

    async connect() {
        try {
            this.connection = await odbc.connect(this.config);
            console.log('成功連接到 DB2 for IBM i');
            return this.connection;
        } catch (error) {
            console.error('連接錯誤:', error);
            throw error;
        }
    }

    async disconnect() {
        if (this.connection) {
            await this.connection.close();
            console.log('連接已關閉');
        }
    }

    async executeQuery(query) {
        try {
            const result = await this.connection.query(query);
            return result;
        } catch (error) {
            console.error('查詢錯誤:', error);
            throw error;
        }
    }
}

// 使用示例
async function testDatabase() {
    const db = new Db2Connection(connectionConfig);
    try {
        await db.connect();

        // 測試新增
        const insertResult = await db.executeQuery(
            "INSERT INTO DDSCINFO.EMAIL (TEAM, EMAILADDR) VALUES ('TEST01', 'test01@example.com')"
        );
        console.log('新增結果:', insertResult);

        // 測試查詢
        const selectResult = await db.executeQuery('SELECT * FROM DDSCINFO.EMAIL LIMIT 5');
        console.log('查詢結果:', selectResult);

        // 測試修改
        const updateResult = await db.executeQuery(
            "UPDATE DDSCINFO.EMAIL SET EMAILADDR = 'TESTUP@example.com' WHERE TEAM = 'TEST01'"
        );
        console.log('修改結果:', updateResult);

        // 測試刪除
        const deleteResult = await db.executeQuery(
            "DELETE FROM DDSCINFO.EMAIL WHERE TEAM = 'TEST01'"
        );
        console.log('刪除結果:', deleteResult);

    } catch (error) {
        console.error('操作錯誤:', error);
    } finally {
        await db.disconnect();
    }
}

testDatabase();