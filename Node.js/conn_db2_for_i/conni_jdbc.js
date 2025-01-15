const { DemoService, DatabaseService, ConfigManager } = require('./index');

// 改進連線池管理
let pool = null;
function createPool() {
  if (pool) {
    return pool;  // 如果已存在則直接返回
  }
  const config = loadConfig();
  pool = jt400.pool(config);
  return pool;
}

// 新增關閉連線池的方法
async function closePool() {
  if (pool) {
    await pool.close();
    pool = null;
  }
}

// 新增統一的錯誤處理類
class DatabaseError extends Error {
  constructor(message, operation, originalError) {
    super(message);
    this.name = 'DatabaseError';
    this.operation = operation;
    this.originalError = originalError;
  }
}

// 確保所有數據庫操作都使用同一個連線池
async function queryAS400(schema, table) {
  if (!pool) {
    createPool();
  }
  try {
    // ... existing code ...
  } catch (err) {
    throw new DatabaseError(
      '查詢失敗',
      'QUERY',
      err
    );
  }
}

// 使用示例
const demoService = new DemoService();
demoService.runDemo('SCHEMA', 'TABLE')
  .then(results => console.log(results))
  .catch(err => console.error(err));