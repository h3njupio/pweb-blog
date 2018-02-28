from selenium import webdriver
import os

TEST_URL = 'https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html'

driver_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'drivers', 'chromedriver')

options = webdriver.ChromeOptions()
options.add_argument('headless')
## headless브라우저로 인식되지 않도록 UserAgent값을 바꿔줍니다.
## headless브라우저 UserAgent값 : User-Agent:  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/64.0.3282.119 Safari/537.36
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36")

driver = webdriver.Chrome(driver_path, chrome_options=options)

## UserAgent값 확인
driver.get(TEST_URL)
user_agent = driver.find_element_by_css_selector('#user-agent').text
print('User-Agent: ', user_agent)

'''
driver.get('http://h3njupio.pythonanywhere.com/blog/')
driver.implicitly_wait(3)
driver.get_screenshot_as_file('wow.png')
'''
driver.quit()