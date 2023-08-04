def reorder_string(input_string):
    if len(input_string) % 4 != 0:
        return "字串長度必須是4的倍數才能均分。"

    quarter_len = len(input_string) // 4
    parts = [input_string[i:i+quarter_len] for i in range(0, len(input_string), quarter_len)]
    reordered_str = parts[1] + parts[2] + parts[0] + parts[3]

    return reordered_str

# 測試
# input_str = "I LIKE TO LEARN PYTHON!!"
input_str =   "$#%YTRTEGBREGBFDBDBDFGBD"
reordered_str = reorder_string(input_str)
print(reordered_str)
