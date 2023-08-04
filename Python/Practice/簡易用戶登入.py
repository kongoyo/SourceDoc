# 如果用戶名稱是kongoyo且密碼為1234則登入成功
while True:
    username=input('請輸入用戶名稱: ')
    password=input('請輸入用戶密碼: ')
    if username=='kongoyo' and password=='1234':
        print('登入成功!')
        break
    else:
        print('登入失敗，重新輸入!')
    continue
