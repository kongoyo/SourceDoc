const express = require('express');
const bodyParser = require('body-parser');
const app = express();

// 設置中間件
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

// 註冊路由
const indexRoute = require('./routes/index');
const usersRoute = require('./routes/users');
app.use('/', indexRoute);
app.use('/users', usersRoute);

// 啟動伺服器
const port = 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
