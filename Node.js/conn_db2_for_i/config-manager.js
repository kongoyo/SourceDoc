const readline = require('readline');
const { loadConfig, updateConfig } = require('./conni_jdbc');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

async function promptConfig() {
  const currentConfig = loadConfig();
  
  console.log('\n目前的設定：');
  console.log(currentConfig);
  
  const questions = [
    ['host', '請輸入 AS400 主機位址'],
    ['user', '請輸入使用者名稱'],
    ['password', '請輸入密碼'],
    ['maxConnections', '請輸入最大連線數'],
    ['connectionTimeout', '請輸入連線逾時時間(毫秒)'],
    ['debug', '是否開啟除錯模式(true/false)']
  ];

  const newConfig = { ...currentConfig };

  for (const [key, question] of questions) {
    const answer = await new Promise(resolve => {
      rl.question(`${question} (目前: ${currentConfig[key]}): `, resolve);
    });
    
    if (answer.trim()) {
      if (key === 'debug') {
        newConfig[key] = answer.toLowerCase() === 'true';
      } else if (key === 'maxConnections' || key === 'connectionTimeout') {
        newConfig[key] = parseInt(answer);
      } else {
        newConfig[key] = answer;
      }
    }
  }

  return newConfig;
}

async function main() {
  try {
    console.log('AS400 連線設定管理工具');
    const newConfig = await promptConfig();
    
    console.log('\n新的設定：');
    console.log(newConfig);
    
    const confirm = await new Promise(resolve => {
      rl.question('\n是否要儲存這些設定？(y/n): ', resolve);
    });

    if (confirm.toLowerCase() === 'y') {
      updateConfig(newConfig);
      console.log('設定已更新');
    } else {
      console.log('取消更新設定');
    }
  } catch (err) {
    console.error('設定更新失敗:', err);
  } finally {
    rl.close();
  }
}

main(); 