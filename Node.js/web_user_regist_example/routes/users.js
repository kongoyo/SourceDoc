const express = require('express');
const router = express.Router();
const User = require('../models/user');

// 註冊頁面路由
router.get('/register', (req, res) => {
  res.render('register');
});

// 處理註冊表單提交
router.post('/register', (req, res) => {
  const { username, password } = req.body;
  const newUser = new User({ username, password });
  newUser.save((err) => {
    if (err) {
      console.error(err);
      res.redirect('/users/register');
    } else {
      res.redirect('/');
    }
  });
});

module.exports = router;
