const jt400 = require('node-jt400');
const random = require('random');

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

async function addRandomRecord(schema, table) {
  try {
    const randomData = {
      name: `User_${random.int(1000, 9999)}`,
      age: random.int(18, 80),
      email: `user_${random.int(1000, 9999)}@example.com`
    };
    
    const sql = `INSERT INTO ${schema}.${table} (name, age, email) VALUES ('${randomData.name}', ${randomData.age}, '${randomData.email}')`;
    const result = await pool.query(sql);
    
    console.log('新增成功');
    return result;

  } catch (err) {
    console.error('新增失敗:', err);
    throw err;
  }
}

async function updateRandomRecord(schema, table) {
  try {
    const sql = `SELECT * FROM ${schema}.${table}`;
    const results = await pool.query(sql);
    
    if (results.length === 0) {
      console.log('沒有記錄可更新');
      return null;
    }
    
    const randomRecord = results[random.int(0, results.length - 1)];
    const updateData = {
      name: `Updated_User_${random.int(1000, 9999)}`,
      age: random.int(18, 80)
    };
    
    const updateSql = `UPDATE ${schema}.${table} SET name = '${updateData.name}', age = ${updateData.age} WHERE id = ${randomRecord.id}`;
    const result = await pool.query(updateSql);
    
    console.log('更新成功');
    return result;

  } catch (err) {
    console.error('更新失敗:', err);
    throw err;
  }
}

async function deleteRandomRecord(schema, table) {
  try {
    const sql = `SELECT * FROM ${schema}.${table}`;
    const results = await pool.query(sql);
    
    if (results.length === 0) {
      console.log('沒有記錄可刪除');
      return null;
    }
    
    const randomRecord = results[random.int(0, results.length - 1)];
    const deleteSql = `DELETE FROM ${schema}.${table} WHERE id = ${randomRecord.id}`;
    const result = await pool.query(deleteSql);
    
    console.log('刪除成功');
    return result;

  } catch (err) {
    console.error('刪除失敗:', err);
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