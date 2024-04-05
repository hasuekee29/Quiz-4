from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

options = Options()
options.add_argument("--window-size=1440,768") 

driver = webdriver.Chrome(options= options)

#前往 台灣證券交易所 頁面 https://www.twse.com.tw/zh/index.html
driver.get("https://www.twse.com.tw/zh/index.html")
driver.find_element(By.LINK_TEXT, "交易資訊").click()
driver.find_element(By.LINK_TEXT, "個股日收盤價及月平均價").click()
time.sleep(2)

#民國
select_object = driver.find_element(By.ID, "label0")
select_object = Select(select_object)
select_object.select_by_visible_text('民國 112 年')
time.sleep(2)

#月
select_object = driver.find_element(By.NAME, "mm")
select_object = Select(select_object)
select_object.select_by_visible_text('01月')
time.sleep(2)

#股票代號2330
stockNo = driver.find_element(By.NAME, "stockNo")
stockNo.send_keys("2330")
time.sleep(2)

#點擊查詢
search = driver.find_element(By.CLASS_NAME, "submit")
search.click()
time.sleep(2)

#print股價
stock_element = driver.find_element(By.CSS_SELECTOR, 'tbody.is-last-page')
stock_data = stock_element.text
for data in stock_data.split("\n")[:-1]:
    print(data)

#移動到stock畫面並截圖
driver.execute_script("arguments[0].scrollIntoView();", stock_element)
time.sleep(2)
stock_element.screenshot("screenshot.png")
