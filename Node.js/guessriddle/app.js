const readline = require('readline');

// 创建接口读取器
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// 定义谜底和对应的提示
const riddles = [
  { answer: '椅子', hint: '坐在上面' },
  { answer: '眼睛', hint: '用来看东西' },
  { answer: '手表', hint: '可以看时间' },
  { answer: '铅笔', hint: '用来写字' }
];

// 随机选择一个谜底
const randomIndex = Math.floor(Math.random() * riddles.length);
const currentRiddle = riddles[randomIndex];

// 开始游戏
console.log('欢迎来到猜灯谜游戏！');
console.log('猜灯谜：');
console.log(currentRiddle.hint);

// 监听用户输入
rl.on('line', (input) => {
  if (input.trim().toLowerCase() === currentRiddle.answer) {
    console.log('恭喜你猜对了！');
    rl.close();
  } else {
    console.log('猜错了，请继续猜！');
  }
});

// 游戏结束时关闭接口读取器
rl.on('close', () => {
  console.log('游戏结束。');
  process.exit();
});
