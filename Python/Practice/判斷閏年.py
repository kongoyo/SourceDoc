year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
is_leap = year % 4 == 0 and year % 100 != 0 or \
          year % 400 == 0

# 顯示is_leap是哪種類型的變數
print(type(is_leap))
# 顯示is_leap的值
print(is_leap)