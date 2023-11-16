from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, value="fName")

f_name.send_keys("Whisper")

l_name = driver.find_element(By.NAME, value="lName")

email = driver.find_element(By.NAME, value="email")

l_name.send_keys("Aradien")

email.send_keys("whisper@email.com")

button = driver.find_element(By.CLASS_NAME, value="btn")

button.click()





