from flask import Flask, render_template, url_for


app = Flask(__name__)

import crawling

from selenium import webdriver


from bs4 import BeautifulSoup

#index

@app.route('/')
def hello():
    myList, myList_href = crawling.daum()
    today, today_href = crawling.today()
    clien, clien_href = crawling.clien()
    blog, blog_href = crawling.blog()
    blog1, blog1_href = crawling.blog1()
    blog2, blog2_href = crawling.blog2()
    blog3, blog3_href = crawling.blog3()
    blog4, blog4_href = crawling.blog4()
    blog5, blog5_href = crawling.blog5()



    return render_template("index.html",
                           list=myList, list_href=myList_href, list_len=len(myList),
                           list2=today, list2_href=today_href, list2_len=len(today),
                           list3=clien, list3_href=clien_href, list3_len=len(clien),
                           list4=blog, list4_href=blog_href, list4_len=len(blog),
                           list5=blog1, list5_href=blog1_href, list5_len=len(blog1),
                           list6=blog2, list6_href=blog2_href, list6_len=len(blog2),
                           list7=blog3, list7_href=blog3_href, list7_len=len(blog3),
                           list8=blog4, list8_href=blog4_href, list8_len=len(blog4),
                           list9=blog5, list9_href=blog5_href, list9_len=len(blog5)

                           )
#index1

@app.route('/about')
def about():


    list_daum, list_daum_href = crawling.daum()
    list_today, list_today_href = crawling.today()
    list_clien, list_clien_href = crawling.clien()



    return render_template("index1.html",
                           daum = list_daum,
                           today = list_today,
                           clien = list_clien,
                           daum_href = list_daum_href,
                           daum_len = len(list_daum),
                           today_len= len(list_today),
                           today_href = list_today_href,
                            clien_href = list_clien_href,
                            clien_len = len(list_clien),
                                        )


@app.route('/mobile')
def mobile():
    myList, myList_href = crawling.daum()
    today, today_href = crawling.today()
    clien, clien_href = crawling.clien()
    blog, blog_href = crawling.blog()
    blog1, blog1_href = crawling.blog1()
    blog2, blog2_href = crawling.blog2()
    blog3, blog3_href = crawling.blog3()

    return render_template("mobile.html",
                           list=myList, list_href=myList_href, list_len=len(myList),
                           list2=today, list2_href=today_href, list2_len=len(today),
                           list3=clien, list3_href=clien_href, list3_len=len(clien),
                           list4=blog, list4_href=blog_href, list4_len=len(blog),
                           list5=blog1, list5_href=blog1_href, list5_len=len(blog1),
                           list6=blog2, list6_href=blog2_href, list6_len=len(blog2),
                           list7=blog3, list7_href=blog3_href,  list7_len=len(blog3))







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)