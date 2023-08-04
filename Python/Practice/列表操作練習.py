def list_operations(nums):
    # 計算列表中所有元素的總和
    total_sum = sum(nums)

    # 計算列表中所有元素的平均值
    average = total_sum / len(nums)

    # 找出列表中的最大值和最小值
    max_num = max(nums)
    min_num = min(nums)

    # 將列表中的元素進行排序
    sorted_nums = sorted(nums)

    return total_sum, average, max_num, min_num, sorted_nums

# 創建一個包含整數元素的列表
my_list = [15, 22, 8, 10, 45, 3, 17]

# 執行列表操作並輸出結果
total_sum, average, max_num, min_num, sorted_nums = list_operations(my_list)

print("列表中所有元素的總和：", total_sum)
print("列表中所有元素的平均值：", average)
print("列表中的最大值：", max_num)
print("列表中的最小值：", min_num)
print("列表排序後：", sorted_nums)
