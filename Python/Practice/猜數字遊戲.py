import random


def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("歡迎來到猜數字遊戲!")
    print("請在1到100之間猜一個數字。")

    while True:
        try:
            user_guess = int(input("請輸入你的猜測: "))
        except ValueError:
            print("請輸入有效的數字!")
            continue

        attempts += 1

        if user_guess < secret_number:
            print("太小了，請再猜一次。")
        elif user_guess > secret_number:
            print("太大了，請再猜一次。")
        else:
            print(f"恭喜你猜對了! 數字是 {secret_number}。你總共猜了 {attempts} 次。")
            break

guess_number()
