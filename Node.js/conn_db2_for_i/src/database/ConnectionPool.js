const jt400 = require('node-jt400');
const ConfigManager = require('../config/ConfigManager');

class ConnectionPool {
  static #instance = null;
  #pool = null;

  static getInstance(hostName = null) {
    if (!ConnectionPool.#instance) {
      ConnectionPool.#instance = new ConnectionPool();
    }
    return ConnectionPool.#instance;
  }

  getPool(hostName = null) {
    if (!this.#pool) {
      const config = ConfigManager.getInstance().loadConfig(hostName);
      this.#pool = jt400.pool(config);
    }
    return this.#pool;
  }

  async query(sql, params = []) {
    const pool = this.getPool();
    try {
      return await pool.query(sql, params);
    } catch (err) {
      throw new Error(`查詢執行失敗: ${err.message}`);
    }
  }

  async execute(sql, params = []) {
    const pool = this.getPool();
    try {
      return await pool.update(sql, params);  // node-jt400 使用 update 方法執行修改操作
    } catch (err) {
      throw new Error(`執行失敗: ${err.message}`);
    }
  }

  async closePool() {
    if (this.#pool) {
      await this.#pool.close();
      this.#pool = null;
    }
  }
}

module.exports = ConnectionPool; 