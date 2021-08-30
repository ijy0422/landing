import requests
from urllib import request
from bs4 import BeautifulSoup
# URL 설정
BASE_URL = "https://gall.dcinside.com/board/view/?id=dcbest&no=2479&page=1"
DOMAIN_URL = "https://gall.dcinside.com"
# 헤더 설정
headers = [
    {'User-Agent' : ''},
]

html_list = requests.get(BASE_URL, headers=headers[0])
soup = BeautifulSoup(html_list.content, 'html.parser')

file_box = soup.find('div', class_='appending_file_box').find_all('li')
num = 0
for i in file_box:
    num += 1 # 넘버링
    img_URL = i.find('a',href=True)['href'] # 이미지 주소
    file_ext = i.find('a',href=True)['href'].split('.')[-1] # 확장자 추출
    opener = request.build_opener()
    opener.addheaders = [('User-agent', ''), ('Referer', html_list.url)]
    request.install_opener(opener)
    request.urlretrieve(img_URL, "TEST" + str(num) + "." + file_ext)

