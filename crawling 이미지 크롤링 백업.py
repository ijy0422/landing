# 크롤링 라이브러리 import
import urllib3


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
    req = requests.get('http://www.newsnjob.com/news/articleList.html?sc_section_code=S1N2&view_type=sm' , verify=False)

    # 이런 식으로 HTML에 있는 코드를 다 가져온다
    soup = BeautifulSoup(req.text, 'html.parser')


    myList = []
    myList_href = []

    for i in soup.select("#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div > div.list-titles"):
        myList.append(i.text)
        myList_href.append("http://www.newsnjob.com/" + i.find("a")["href"])

    return myList, myList_href


def blog():
    # 엔터치기
    req = requests.get('https://bvutf66khjg2.tistory.com/')

    # 이런 식으로 HTML에 있는 코드를 다 가져온다
    soup = BeautifulSoup(req.text, 'html.parser')


    blog = []
    blog_href = []

    for i in soup.select("#content > div.inner > div:nth-child(1)"):
        blog.append(i.find("span", class_="title").text)
        blog_href.append("https://bvutf66khjg2.tistory.com/" + i.find("a")["href"])


    return blog, blog_href


def blog1():
    # 엔터치기
    req = requests.get('https://bvutf66khjg2.tistory.com/')

    # 이런 식으로 HTML에 있는 코드를 다 가져온다
    soup = BeautifulSoup(req.text, 'html.parser')


    blog1 = []
    blog1_src = []
    blog1_href = []

    for i in soup.select("#content > div.inner > div:nth-child(1)"):

        blog1.append(i.find("img")["src"])
        blog1_href.append("https://bvutf66khjg2.tistory.com" + i.find("a")["href"])
        blog1_src.append(i.find("img")["src"])

    return blog1, blog1_href, blog1_src



def blog2():
    # 엔터치기
    req = requests.get('https://bvutf66khjg2.tistory.com/')

    # 이런 식으로 HTML에 있는 코드를 다 가져온다
    soup = BeautifulSoup(req.text, 'html.parser')


    blog2 = []
    blog2_href = []

    for i in soup.select("#content > div.inner > div:nth-child(2)"):
        blog2.append(i.find("span", class_="title").text)
        blog2_href.append("https://bvutf66khjg2.tistory.com/" + i.find("a")["href"])


    return blog2, blog2_href


def blog3():
    # 엔터치기
    req = requests.get('https://bvutf66khjg2.tistory.com/')

    # 이런 식으로 HTML에 있는 코드를 다 가져온다
    soup = BeautifulSoup(req.text, 'html.parser')


    blog3 = []
    blog3_src = []
    blog3_href = []

    for i in soup.select("#content > div.inner > div:nth-child(2)"):

        blog3.append(i.find("img")["src"])
        blog3_href.append("https://bvutf66khjg2.tistory.com" + i.find("a")["href"])
        blog3_src.append(i.find("img")["src"])

    return blog3, blog3_href, blog3_src


def blog4():
    # 엔터치기
    req = requests.get('https://bvutf66khjg2.tistory.com/')

    # 이런 식으로 HTML에 있는 코드를 다 가져온다
    soup = BeautifulSoup(req.text, 'html.parser')


    blog4 = []
    blog4_href = []

    for i in soup.select("#content > div.inner > div:nth-child(3)"):
        blog4.append(i.find("span", class_="title").text)
        blog4_href.append("https://bvutf66khjg2.tistory.com/" + i.find("a")["href"])


    return blog4, blog4_href


def blog5():
    # 엔터치기
    req = requests.get('https://bvutf66khjg2.tistory.com/')

    # 이런 식으로 HTML에 있는 코드를 다 가져온다
    soup = BeautifulSoup(req.text, 'html.parser')


    blog5 = []
    blog5_src = []
    blog5_href = []

    for i in soup.select("#content > div.inner > div:nth-child(3)"):

        blog5.append(i.find("img")["src"])
        blog5_href.append("https://bvutf66khjg2.tistory.com" + i.find("a")["href"])
        blog5_src.append(i.find("img")["src"])

    return blog5, blog5_href, blog5_src

