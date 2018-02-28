import requests
from bs4 import BeautifulSoup
import time

## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "PWEB.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()
## BlogData를 import해옵니다
from parsed_data.models import BlogData

import telegram
from PWEB import settings
bot = telegram.Bot(token=settings.TELE_TOKEN)
chat_id = bot.getUpdates()[-1].message.chat_id

data_dir = os.path.join(os.path.dirname(os.path.abspath('__file__')), 'data')

def parse_blog():
    req = requests.get('http://h3njupio.pythonanywhere.com/blog/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select(
        'body > div.content.container > div > div > div > h1 > a'
    )
    recent = titles[-1]

    with open(os.path.join(data_dir, 'etc', 'recent.txt'), 'r') as r_file:
        latest = r_file.readline()
        if latest != recent.text:
            BlogData(title=recent.text, link=recent.get('href')).save()
            bot.send_message(chat_id=chat_id, text='[알림] 새 글이 등록되었습니다.\n'+recent.text)
            with open(os.path.join(data_dir, 'etc', 'recent.txt'), 'w+') as w_file:
                w_file.write(recent.text)




'''
    data = {}

    for title in titles:
        data[title.text] = title.get('href')
    return data
'''

if __name__ == '__main__':
    while True:
        blog_data_dict = parse_blog()
        time.sleep(30)

'''
    for t, l in blog_data_dict.items():
        BlogData(title = t, link = l).save()
'''