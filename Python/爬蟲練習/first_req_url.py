from urllib.request import urlopen

url = "https://www.baidu.com"
resp = urlopen(url)

# 網頁內包含cp950無法辨識的字元，故open內需加入encoding='utf-8'，因此需要將全部字元從unicode改為cp950再輸出
with open("mybaidu.html", mode="w", encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))
    print("over!")
