from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

Youtube_Trending_URL = "https://www.youtube.com/feed/trending"


def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  #chrome_options.add_argument('headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver


def get_videos(driver):
  video_divs_tag = "ytd-video-renderer"
  driver.get(Youtube_Trending_URL)
  time.sleep(10)
  videos = driver.find_elements(By.TAG_NAME, video_divs_tag)
  return videos


def parse_video(video):
  title_tag = video.find_element(By.ID, "video-title")
  title = title_tag.text

  url = title_tag.get_attribute('href')

  channel_name_tag = video.find_element(By.TAG_NAME, "ytd-channel-name")
  channel_name = channel_name_tag.text

  description = video.find_element(By.ID, "description-text").text
  return {
    "title": title,
    "url": url,
    "channel name": channel_name,
    "description": description
  }


if __name__ == "__main__":
  print("Creating driver")
  driver = get_driver()
  print("Fetching trending Videos")
  videos = get_videos(driver)
  print(f'Found {len(videos)} Videos')
  print("Parsing top 10 videos")
  videos_data=[parse_video(video) for video in videos[:10]]
  #title , url , thumbnail_url , channal , views , uploaded , description
  #print(videos_data)
  print(videos_data[3])
  ##saving to csv file 
  videos_df=pd.DataFrame(videos_data)
  print(videos_df)
  ##save to csv 
  videos_df.to_csv('trending.csv')
  


  
