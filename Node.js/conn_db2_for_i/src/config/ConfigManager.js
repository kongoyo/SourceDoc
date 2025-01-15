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

  loadConfig(hostName = null) {
    try {
      const configPath = path.join(__dirname, '../../config.json');
      const fullConfig = JSON.parse(fs.readFileSync(configPath, 'utf8')).as400;
      
      if (!this.#config) {
        this.#config = fullConfig;
      }

      if (hostName) {
        if (!this.#config.hosts[hostName]) {
          throw new Error(`找不到主機配置: ${hostName}`);
        }
        return this.#config.hosts[hostName];
      }
      
      return this.#config.hosts[this.#config.defaultHost];
    } catch (err) {
      throw new Error('讀取設定檔失敗: ' + err.message);
    }
  }

  updateConfig(newConfig, hostName) {
    try {
      const configPath = path.join(__dirname, '../../config.json');
      const fullConfig = JSON.parse(fs.readFileSync(configPath, 'utf8'));
      
      if (!hostName) {
        hostName = fullConfig.as400.defaultHost;
      }

      fullConfig.as400.hosts[hostName] = newConfig;
      fs.writeFileSync(configPath, JSON.stringify(fullConfig, null, 2), 'utf8');
      this.#config = fullConfig.as400;
      console.log(`設定檔更新成功 (主機: ${hostName})`);
    } catch (err) {
      throw new Error('更新設定檔失敗: ' + err.message);
    }
  }

  getAvailableHosts() {
    const config = this.loadConfig();
    return Object.keys(this.#config.hosts);
  }

  setDefaultHost(hostName) {
    try {
      const configPath = path.join(__dirname, '../../config.json');
      const fullConfig = JSON.parse(fs.readFileSync(configPath, 'utf8'));
      
      if (!fullConfig.as400.hosts[hostName]) {
        throw new Error(`找不到主機配置: ${hostName}`);
      }

      fullConfig.as400.defaultHost = hostName;
      fs.writeFileSync(configPath, JSON.stringify(fullConfig, null, 2), 'utf8');
      this.#config = fullConfig.as400;
      console.log(`預設主機已更新為: ${hostName}`);
    } catch (err) {
      throw new Error('更新預設主機失敗: ' + err.message);
    }
  }
}

module.exports = ConfigManager; 