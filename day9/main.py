from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'C:/Users/Sardor/Downloads/chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

elements = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
element_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget a')

events = {}

for n in range(len(elements)):
    events[n] = {
        "time": elements[n].text, 
        "name": element_names[n].text
    }

print(events)

driver.quit()