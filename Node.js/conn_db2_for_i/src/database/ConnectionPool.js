const jt400 = require('node-jt400');
const ConfigManager = require('../config/ConfigManager');
const fs = require('fs');
const logFilePath = 'coni_jdbc.log';

// Function to get the current timestamp and PID
function getLogHeader() {
  const date = new Date();
  return `${date.toISOString()} [PID: ${process.pid}]`;
}

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
      const result = await pool.query(sql, params);
      fs.appendFileSync(logFilePath, `${getLogHeader()} QUERY EXECUTED: ${sql} with params: ${params}\n`);
      return result;
    } catch (err) {
      throw new Error(`查詢執行失敗: ${err.message}`);
    }
  }

  async execute(sql, params = []) {
    const pool = this.getPool();
    try {
      const result = await pool.update(sql, params);
      fs.appendFileSync(logFilePath, `${getLogHeader()} EXECUTE: ${sql} with params: ${params}\n`);
      return result;
    } catch (err) {
      throw new Error(`執行失敗: ${err.message}`);
    }
  }
}

module.exports = ConnectionPool;