from django.shortcuts import render
from bs4 import BeautifulSoup
from selenium import webdriver
from appium import webdriver as mobiledriver
import os

def misc_list(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        driver = m_chrome_driver()
        wfms(driver, user_id, user_pw)

    elif request.method == 'GET':
        return render(request, 'misc/misc_list.html')


def chrome_driver():
    ## 옵션
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    ## headless브라우저로 인식되지 않도록 UserAgent값 변경
    ## headless브라우저 UserAgent값 : User-Agent:  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/64.0.3282.119 Safari/537.36
    options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36")

    ## 드라이버생성
    #chrome_driver = webdriver.Chrome(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'driver', 'chromedriver'), chrome_options=options)
    chrome_driver = webdriver.Chrome(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'driver', 'chromedriver'))
    return chrome_driver


def m_chrome_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.2'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['app'] = '../../../apps/selendroid-test-app.apk'

    m_chrome_driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return m_chrome_driver


def wfms(driver, user_id, user_pw):
    ## 근태관리시스템
    url = 'https://infra.bnksys.co.kr'
    driver.get(url)
    driver.find_element_by_id('text_id').send_keys(user_id)
    driver.find_element_by_id('text_password').send_keys(user_pw)

    ## insert value into hidden element
    driver.execute_script("document.getElementById('externalIP').value='210.183.119.193'")
    driver.find_element_by_class_name('login_btn').click()

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    location = soup.select('div.location > h1')

    return location[0].text