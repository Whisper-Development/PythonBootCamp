from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep the browser opened
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.amazon.it/Logitech-Personalizzabili-Connettivit%C3%A0-Compatibilit%C3%A0-Multidispositivo/dp/B07W7LFHH9/ref=sr_1_28?crid=TE2F3XDNB0BI&keywords=tastiera%2Blogitech&qid=1700137492&sprefix=logipop%2Caps%2C130&sr=8-28&th=1")

price_euros = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(f"The price is {price_euros.text}.{price_cents.text}€")

search_bar = driver.find_element(By.NAME, value="field-keywords")

button = driver.find_element(By.ID, value="nav-search-submit-button")

#We can also use By.Css selector, if the element doesn't have a class or id

driver.quit()
