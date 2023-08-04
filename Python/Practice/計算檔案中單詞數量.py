def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"找不到檔案 '{filename}'。")
        return None

# 讓使用者輸入檔案的路徑
file_path = input("請輸入檔案的路徑：")

# 預設檔案名稱
file_name = 'text.txt'

# 呼叫函式並取得單詞數量
word_count = count_words(file_path+"\\"+file_name)

if word_count is not None:
    print(f"檔案中的單詞數量為：{word_count}")
