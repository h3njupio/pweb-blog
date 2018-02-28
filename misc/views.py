from django.shortcuts import render
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import platform

def misc_list(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        platform_type = request.POST['platform_type']

        result = ""
        if platform_type == "PC":
            driver = chrome_driver()
            result = wfms(driver, user_id, user_pw)
        elif platform_type == "MOBILE":
            result = m_chrome_driver(user_id, user_pw)

        if str(platform.system()).upper() == 'WINDOWS':
            driver = 'chromedriver.exe'
        else:
            driver = 'chromedriver'

        return render(request, 'misc/misc_list.html', {'status':result, 'os':driver})

    elif request.method == 'GET':
        return render(request, 'misc/misc_list.html')


def chrome_driver():
    ## 옵션
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    ## headless브라우저로 인식되지 않도록 UserAgent값 변경
    ## headless브라우저 UserAgent값 : User-Agent:  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/64.0.3282.119 Safari/537.36
    options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36")

    if str(platform.system()).upper() == 'WINDOWS':
        driver = 'chromedriver.exe'
    else:
        driver = 'chromedriver'

    ## 드라이버생성
    chrome_driver = webdriver.Chrome(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'driver', ''), chrome_options=options)
    #chrome_driver = webdriver.Chrome(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'driver', 'chromedriver'))
    return chrome_driver


def m_chrome_driver(user_id, user_pw):
    desired_caps = {}
    desired_caps['testdroid_username'] = 'ville - veikko.helppi @ bitbar.com'
    desired_caps['testdroid_password'] = 'xxxxxxxx'
    desired_caps['testdroid_target'] = 'chrome'
    desired_caps['testdroid_project'] = 'Appium Chrome'
    desired_caps['testdroid_testrun'] = 'TestRun 1'
    desired_caps['testdroid_device'] = 'Asus Google Nexus 7 (2013) ME571KL'
    desired_caps['platformName'] = 'android'
    desired_caps['deviceName'] = 'AndroidDevice'
    desired_caps['browserName'] = 'chrome'

    m_chrome_driver = mobiledriver.Remote('https://infra.bnksys.co.kr', desired_caps)
    m_chrome_driver.driver.find_element_by_id('text_id').send_keys(user_id)
    m_chrome_driver.find_element_by_id('text_password').send_keys(user_pw)
    m_chrome_driver.execute_script("document.getElementById('externalIP').value='210.183.119.193'")
    m_chrome_driver.find_element_by_class_name('login_btn').click()

    html = m_chrome_driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    location = soup.select('div.location > h1')
    m_chrome_driver.quit()

    return location[0].text


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
    driver.quit()

    return location[0].text