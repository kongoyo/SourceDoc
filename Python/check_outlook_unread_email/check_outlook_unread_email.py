import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")


def process_folder(folder):
    for item in folder.Items:
        if item.UnRead:
            print(f"主旨：{item.Subject}")

            if item.Body:
                print(f"內文：{item.Body}")
            elif item.HTMLBody:
                print(f"內文：{item.HTMLBody}")

            print("=" * 40)

    for subfolder in folder.Folders:
        process_folder(subfolder)


# 遍歷DDSC根資料夾的每個子資料夾
root_folder = outlook.Folders.Item("DDSC")
for subfolder in root_folder.Folders:
    process_folder(subfolder)
