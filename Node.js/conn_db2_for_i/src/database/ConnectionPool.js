const jt400 = require('node-jt400');
const ConfigManager = require('../config/ConfigManager');

class ConnectionPool {
  static #instance = null;
  #pool = null;

  static getInstance() {
    if (!ConnectionPool.#instance) {
      ConnectionPool.#instance = new ConnectionPool();
    }
    return ConnectionPool.#instance;
  }

  getPool() {
    if (!this.#pool) {
      const config = ConfigManager.getInstance().loadConfig();
      this.#pool = jt400.pool(config);
    }
    return this.#pool;
  }

  async closePool() {
    if (this.#pool) {
      await this.#pool.close();
      this.#pool = null;
    }
  }
}

module.exports = ConnectionPool; 