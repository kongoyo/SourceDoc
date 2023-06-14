const readline = require('readline');

// 設定遊戲畫面大小
const width = 10;
const height = 10;

// 初始化遊戲狀態
let snake = [{ x: 5, y: 5 }];
let direction = { x: 1, y: 0 };
let food = { x: Math.floor(Math.random() * width), y: Math.floor(Math.random() * height) };

// 建立介面讀取器
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// 監聽鍵盤輸入
rl.input.on('keypress', (str, key) => {
  if (key.name === 'w' && direction.y !== 1) {
    direction = { x: 0, y: -1 };
  } else if (key.name === 's' && direction.y !== -1) {
    direction = { x: 0, y: 1 };
  } else if (key.name === 'a' && direction.x !== 1) {
    direction = { x: -1, y: 0 };
  } else if (key.name === 'd' && direction.x !== -1) {
    direction = { x: 1, y: 0 };
  }
});

// 更新遊戲狀態
function update() {
  const head = { x: snake[0].x + direction.x, y: snake[0].y + direction.y };
  
  // 檢查是否撞牆或撞到自己的身體
  if (head.x < 0 || head.x >= width || head.y < 0 || head.y >= height || isCollidingWithSelf(head)) {
    console.log('遊戲結束！');
    process.exit();
  }
  
  // 檢查是否吃到食物
  if (head.x === food.x && head.y === food.y) {
    // 將蛇身延長一格
    snake.unshift(head);
    // 生成新的食物位置
    food = { x: Math.floor(Math.random() * width), y: Math.floor(Math.random() * height) };
  } else {
    // 移動蛇身
    snake.unshift(head);
    snake.pop();
  }
}

// 檢查蛇是否撞到自己的身體
function isCollidingWithSelf(head) {
  for (let i = 1; i < snake.length; i++) {
    if (head.x === snake[i].x && head.y === snake[i].y) {
      return true;
    }
  }
  return false;
}

// 繪製遊戲畫面
function render() {
  let output = '';
  
  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      // 檢查是否為蛇身或食物位置
      if (x === food.x && y === food.y) {
        output += 'o ';
      } else if (isSnakeBody(x, y)) {
        output += 'x ';
      } else {
        output += '. ';
      }
    }
    output += '\n';
  }
  
  console.clear();
  console.log(output);
}

// 檢查指定位置是否為蛇身
function isSnakeBody(x, y) {
  for (let i = 0; i < snake.length; i++) {
    if (snake[i].x === x && snake[i].y === y) {
      return true;
    }
  }
  return false;
}

// 開始遊戲迴圈
setInterval(() => {
  update();
  render();
}, 200);
