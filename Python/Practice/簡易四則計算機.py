def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "無法除以零"
    return x / y

def calculator():
    print("歡迎使用簡單計算器！")
    print("請輸入兩個數字和一個運算符，用空格隔開。")
    print("運算符包括：+ (加法)、- (減法)、* (乘法)、/ (除法)")

    user_input = input("請輸入計算式：")
    parts = user_input.split()

    if len(parts) != 3:
        print("輸入錯誤！請輸入兩個數字和一個運算符，用空格隔開。")
        return

    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        print("無效的運算符！請使用 +、-、*、/ 中的一個。")
        return

    print("計算結果：", result)

calculator()
