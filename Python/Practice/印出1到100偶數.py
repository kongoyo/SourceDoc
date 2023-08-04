# 除以2為0表示偶數
# 解法1
num = 1
while num < 101:
    if num % 2 == 0:
        print(num)
    num +=1

# 解法2
for num in range(1, 101):
    if num % 2 == 0:
        print(num)