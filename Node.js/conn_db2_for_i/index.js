const DemoService = require('./src/demo/DemoService');
const ConnectionPool = require('./src/database/ConnectionPool');

async function main() {
  const schema = process.argv[2] || 'DDSCINFO';
  const table = process.argv[3] || 'EMAIL';

  console.log(`使用 schema: ${schema}, table: ${table}`);
  
  try {
    const demoService = new DemoService();
    const results = await demoService.runDemo(schema, table);
    console.log('示範執行完成:', results);
  } catch (err) {
    console.error('示範執行失敗:', err);
    process.exit(1);
  } finally {
    // 確保關閉連線池
    await ConnectionPool.getInstance().closePool();
  }
}

if (require.main === module) {
  main();
}

module.exports = {
  DemoService,
  DatabaseService: require('./src/services/DatabaseService'),
  ConfigManager: require('./src/config/ConfigManager')
}; 