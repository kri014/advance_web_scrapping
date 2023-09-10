# open google
# search campusx
# learn.withcampusx.in
# DSMP page course
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


s = Service("C:/Users/91993/Desktop/web/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=s)

driver.get("https://www.google.co.in")
time.sleep(2)

# fetch the search input box using xpath
user_input =driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
user_input.send_keys("campusx")
time.sleep(1)

# selecting keys
user_input.send_keys(Keys.ENTER)
time.sleep(1)
link=driver.find_element(by=By.XPATH,value='//*[@id="rso"]/div[1]/div/div/table/tbody/tr[1]/td/div/h3/a')
link.click()
time.sleep(1)

link1=driver.find_element(by=By.XPATH,value="/html/body/div[1]/header/section[2]/a[4]")
link1.click()

