const jt400 = require('node-jt400');

const pool = jt400.pool({
  host: '172.16.13.58',
  user: 'ibmecs',
  password: 'ibmecsusr'
});

async function queryAS400(schema, table) {
  try {
    console.log('正在嘗試連接 AS400...');
    
    // 使用參數構建 SQL 查詢
    const sql = `SELECT * FROM ${schema}.${table}`;
    const results = await pool.query(sql);
    
    console.log('查詢成功');
    return results;

  } catch (err) {
    console.error('AS400 查詢失敗:', err);
    throw err;
  }
}

// 從命令行獲取參數，設定預設值
const schema = process.argv[2] || 'DDSCINFO';
const table = process.argv[3] || 'ALLOBJN';

// 修改檢查邏輯
console.log(`使用 schema: ${schema}, table: ${table}`);

// 執行查詢
queryAS400(schema, table)
  .then(results => {
    console.log('查詢結果:', results);
    process.exit(0);
  })
  .catch(err => {
    console.error('查詢執行失敗:', err);
    process.exit(1);
  });