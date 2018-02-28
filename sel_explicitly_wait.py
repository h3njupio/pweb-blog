from selenium import webdriver
# 아래 코드들을 import 해 줍시다.
from selenium.webdriver.common.by import By
# WebDriverWait는 Selenium 2.4.0 이후 부터 사용 가능
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions는 Selenium 2.26.0 이후 부터 사용 가능
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('chromedriver')

driver.get('https://www.kakaobank.com/')

try:
    # WebDriverWait와 .until 옵션을 통해 우리가 찾고자 하는 HTML 요소를
    # 기다려 줄 수 있습니다.
    title = WebDriverWait(driver, 10) \
        .until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.intro_main > h3")))
    print(title.text)
finally:
    driver.quit()