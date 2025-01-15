const ConnectionPool = require('../database/ConnectionPool');
const DatabaseError = require('../errors/DatabaseError');

class DatabaseService {
  constructor(hostName = null) {
    this.pool = ConnectionPool.getInstance(hostName);
  }

  async query(schema, table) {
    try {
      console.log('正在嘗試連接 AS400...');
      const sql = `SELECT * FROM ${schema}.${table}`;
      const results = await this.pool.query(sql);
      console.log('查詢成功');
      return results;
    } catch (err) {
      if (err.message?.includes('SQL0204')) {
        throw new DatabaseError(
          `找不到 ${schema} 中的 ${table} 類型 *FILE`,
          'QUERY',
          err
        );
      }
      throw new DatabaseError('查詢失敗', 'QUERY', err);
    }
  }

  async addRandomRecord(schema, table) {
    try {
      const randomNum = Math.floor(Math.random() * 9000) + 1000;
      const sql = `INSERT INTO ${schema}.${table} (TEAM, EMAILADDR) VALUES (?, ?)`;
      const values = [
        `Team_${randomNum}`,
        `team_${randomNum}@example.com`
      ];
      
      const result = await this.pool.execute(sql, values);
      return result;
    } catch (err) {
      throw new DatabaseError('新增失敗', 'INSERT', err);
    }
  }

  async updateRandomRecord(schema, table) {
    try {
      const results = await this.query(schema, table);
      
      if (results.length === 0) {
        console.log('沒有記錄可更新');
        return null;
      }
      
      const randomRecord = results[Math.floor(Math.random() * results.length)];
      const updateData = {
        TEAM: `Updated_Team_${Math.floor(Math.random() * 9000) + 1000}`,
        EMAILADDR: `updated_team_${Math.floor(Math.random() * 9000) + 1000}@example.com`
      };
      
      const sql = `UPDATE ${schema}.${table} SET TEAM = ?, EMAILADDR = ? WHERE TEAM = ?`;
      const result = await this.pool.execute(sql, [updateData.TEAM, updateData.EMAILADDR, randomRecord.TEAM]);
      console.log('更新成功');
      return result;
    } catch (err) {
      throw new DatabaseError('更新失敗', 'UPDATE', err);
    }
  }

  async deleteRandomRecord(schema, table) {
    try {
      const results = await this.query(schema, table);
      
      if (results.length === 0) {
        console.log('沒有記錄可刪除');
        return null;
      }
      
      const randomRecord = results[Math.floor(Math.random() * results.length)];
      const sql = `DELETE FROM ${schema}.${table} WHERE TEAM = ?`;
      const result = await this.pool.execute(sql, [randomRecord.TEAM]);
      console.log('刪除成功');
      return result;
    } catch (err) {
      throw new DatabaseError('刪除失敗', 'DELETE', err);
    }
  }
}

module.exports = DatabaseService; 