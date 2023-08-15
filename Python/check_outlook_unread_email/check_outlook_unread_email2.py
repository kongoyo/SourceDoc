import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# 設定根資料夾名稱
root_folders = ["DDSC", "GMAIL"]

# 遍歷指定的根資料夾
for root_folder_name in root_folders:
    root_folder = outlook.Folders(root_folder_name)

    # 遍歷根資料夾下的所有資料夾
    for folder in root_folder.Folders:
        # 遞迴檢查資料夾及其子資料夾的郵件
        def process_folder(folder):
            unread_items = folder.Items.Restrict("[UnRead]=True")
            for item in unread_items:
                print(f"主旨：{item.Subject}")

                # 如果內文是純文本，顯示內文
                if item.BodyFormat == 2:  # 純文本格式
                    print("內文：")
                    print(item.Body)
                else:
                    print("內文：（無法直接顯示）")
                print("=" * 40)

        process_folder(folder)

        # 遞迴處理子資料夾
        def process_subfolders(parent_folder):
            for subfolder in parent_folder.Folders:
                process_folder(subfolder)
                process_subfolders(subfolder)

        process_subfolders(folder)
