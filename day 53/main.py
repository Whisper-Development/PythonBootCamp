from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

website_url = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(website_url)

data = response.text
soup = BeautifulSoup(data, "html.parser")

#Create a list of all the links on the pase using a CSS selector

all_links_elements = soup.select(".StyledPropertyCardDataWrapper a")

all_links = [link["href"] for link in all_links_elements]

print(f"There are {len(all_links)} links to individual listing in total: \n")
print(all_links)


#Create a list of all the addresses on the page using a CSS selector
#Remove newlines \n, pipe symbols |, and whitespaces to clean up the address data

all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")

all_addresses = [address.get_text().replace("|", " ").strip() for address in all_address_elements]
print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")
print(all_addresses)

#Create a list of all the prices on the page using a CSS selector
#Get a clean dollar price and strip off any "+" symbols and "per month" /mo abbreviation

all_price_elements = soup.select(".PropertyCardWrapper span")

all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")
print(all_prices)

#Now that I have 3 lists with the data I need to fill up the forms, I use Selenium

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSchwvC8tNolDYO4ddh755Qan3f2CgMkagulmW5lcoTsmbiQOA/viewform?usp=sf_link")
    time.sleep(2)

    address = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    price = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    
    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()
