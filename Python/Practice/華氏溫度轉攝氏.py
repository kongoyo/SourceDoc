#將華氏溫度轉換為攝氏溫度
#Version: 0.1

f = float(input('請輸入華氏温度: '))
c = (f - 32) / 1.8
print('%.1f華氏溫度 = %.1f攝氏溫度' % (f, c))