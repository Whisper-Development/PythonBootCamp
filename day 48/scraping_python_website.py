from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

upcoming_events = {}

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget.last time")

for time in event_times:
    print(time.text)

driver.quit()