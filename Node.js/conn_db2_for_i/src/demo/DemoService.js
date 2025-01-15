const DatabaseService = require('../services/DatabaseService');

class DemoService {
  constructor(hostName = null) {
    this.dbService = new DatabaseService(hostName);
  }

  async runDemo(schema, table) {
    try {
      console.log('開始執行完整 CRUD 示範...');
      
      console.log('\n步驟 1: 新增記錄');
      const insertResult = await this.dbService.addRandomRecord(schema, table);
      
      console.log('\n步驟 2: 查詢記錄');
      const queryResult = await this.dbService.query(schema, table);
      console.log('當前所有記錄:', queryResult);
      
      console.log('\n步驟 3: 更新記錄');
      const updateResult = await this.dbService.updateRandomRecord(schema, table);
      
      console.log('\n步驟 4: 刪除記錄');
      const deleteResult = await this.dbService.deleteRandomRecord(schema, table);
      
      console.log('\nCRUD 示範完成！');
      return {
        insert: insertResult,
        query: queryResult,
        update: updateResult,
        delete: deleteResult
      };
    } catch (err) {
      console.error('CRUD 示範過程發生錯誤:', err);
      throw err;
    }
  }
}

module.exports = DemoService; 