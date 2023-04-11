from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'C:/Users/Sardor/Downloads/chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

element = driver.find_element(By.LINK_TEXT, '//*[@id="articlecount"]/a[1]')

print(element.text)