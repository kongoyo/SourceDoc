from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from urllib.request import urlopen

option: Options = Options()
# 操作網頁是不顯示網頁 manipulate the browser invisibly
# option.add_argument("-headless")
driver_path = 'E:/Downloads/chrome-win64/chrome-win64/chrome.exe'
chrome = webdriver.Chrome()
chrome.get("https://www.ibm.com/servers/eserver/ess/landing/index.html")
chrome.find_element()
email = chrome.find_element("id", "email")
password = chrome.find_element("id", "pass")

time.sleep(5)
email.send_keys('xxxxx@gmail.com')
password.send_keys('xxxxxx')
password.submit()

# 關閉瀏覽器 close the browser
# chrome.close()
