from openpyxl import Workbook
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

url = "https://mail.naver.com/#%7B%22fClass%22%3A%22list%22%2C%22oParameter%22%3A%7B%22page%22%3A1%2C%22sortField%22%3A1%2C%22sortType%22%3A0%2C%22folderSN%22%3A%22-1%22%2C%22type%22%3A%22all%22%2C%22isUnread%22%3Afalse%7D%7D"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

# ul태그 정보안의 각 기사 정보 가져오기

articles = soup.select("#list_for_view > ol")

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사"])

# 각 기사의 제목 정보 가져오기

for article in articles:
    title = article.select_one('#list_for_view > ol > li.\38 2672_li.mark._c1\(mrCore\|clickTitle\|82672\)._d2\(mcDragndrop\|html5DragStart\) > div').text
    url = article.select_one('#list_for_view > ol > li.\38 2672_li.mark._c1\(mrCore\|clickTitle\|82672\)._d2\(mcDragndrop\|html5DragStart\) > div > div.subject > a._d2\(mcDragndrop\|html5DragStart\)')['href'] # url
    comp = article.select_one('#sp_nws_all1 > div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a.info.press').text
    ws1.append([title, url, comp])

    wb.save(filename='ticles.xlsx')

    driver.quit()
