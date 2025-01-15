const fs = require('fs');
const path = require('path');

class ConfigManager {
  static #instance = null;
  #config = null;

  static getInstance() {
    if (!ConfigManager.#instance) {
      ConfigManager.#instance = new ConfigManager();
    }
    return ConfigManager.#instance;
  }

  loadConfig() {
    if (this.#config) return this.#config;
    try {
      const configPath = path.join(__dirname, '../../config.json');
      this.#config = JSON.parse(fs.readFileSync(configPath, 'utf8')).as400;
      return this.#config;
    } catch (err) {
      throw new Error('讀取設定檔失敗: ' + err.message);
    }
  }

  updateConfig(newConfig) {
    try {
      const configPath = path.join(__dirname, '../../config.json');
      const config = { as400: newConfig };
      fs.writeFileSync(configPath, JSON.stringify(config, null, 2), 'utf8');
      this.#config = newConfig;
      console.log('設定檔更新成功');
    } catch (err) {
      throw new Error('更新設定檔失敗: ' + err.message);
    }
  }
}

module.exports = ConfigManager; 