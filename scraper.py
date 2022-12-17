from selenium import webdriver 

Youtube_Trending_URL = "https://www.youtube.com/feed/trending"

driver = webdriver.Chrome()

driver.get(Youtube_Trending_URL)

print(driver.title)