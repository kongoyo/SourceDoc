const DemoService = require('./src/demo/DemoService');
const ConnectionPool = require('./src/database/ConnectionPool');

async function main() {
  const hostName = process.argv[2] || '172.16.13.58';
  const schema = process.argv[3] || 'DDSCINFO';
  const table = process.argv[4] || 'EMAIL';

  console.log(`使用主機: ${hostName || '預設'}, schema: ${schema}, table: ${table}`);
  
  try {
    const demoService = new DemoService(hostName);
    const results = await demoService.runDemo(schema, table);
    console.log('示範執行完成:', results);
    process.exit(0);
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