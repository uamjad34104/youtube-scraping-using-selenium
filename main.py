from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

Youtube_Trending_URL = "https://www.youtube.com/feed/trending"

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver


if __name__=="__main__":
  print("Creating driver")
  driver=get_driver()
  print("Fetching the page")
  driver.get(Youtube_Trending_URL)

  print("Page Title: " ,driver.title)