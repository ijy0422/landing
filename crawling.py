# 크롤링 라이브러리 import
import requests
from bs4 import BeautifulSoup

def daum() :
    # 엔터치기
    req = requests.get('https://www.mss.go.kr/site/smba/ex/bbs/List.do?cbIdx=310', verify=False)

    soup = BeautifulSoup(req.text, 'html.parser')

    list_daum = []
    list_daum_href = []

    for i in soup.select("#contents_inner > div > table > tbody > tr"):
        list_daum.append(i.find("a").text)
        list_daum_href.append(i.find("a")["href"])

    return list_daum, list_daum_href


def today() :
    # 엔터치기
    req = requests.get('https://www.kised.or.kr/misAnnouncement/index.es?mid=a10302000000' , verify=False)

    # 이런 식으로 HTML에 있는 코드를 다 가져온다
    soup = BeautifulSoup(req.text, 'html.parser')

    list_today = []
    list_today_href = []

    for i in soup.select("#txt > ul > li") :
        list_today.append(i.find("a").text)
        list_today_href.append(i.find("a")["href"])

    return list_today, list_today_href


def clien():
    # 엔터치기
    req = requests.get('https://www.clien.net/service/recommend')

    # 이런 식으로 HTML에 있는 코드를 다 가져온다
    soup = BeautifulSoup(req.text, 'html.parser')

    clien_list = []
    clien_list_href = []

    for i in soup.find_all("span", class_="subject_fixed") :
        clien_list.append(i.text)

        for i in soup.find_all("a", class_="list_subject"):
            clien_list_href.append("https://www.clien.net" + i["href"])

    return clien_list, clien_list_href

