from flask import Flask, render_template, url_for

app = Flask(__name__)

import crawling

#index

@app.route('/')
def hello():

    list_daum, list_daum_href = crawling.daum()
    list_today, list_today_href = crawling.today()
    list_clien, list_clien_href = crawling.clien()

    return render_template("index.html",
                           daum = list_daum,
                           today = list_today,
                           clien = list_clien,
                           daum_href = list_daum_href,
                           daum_len = len(list_daum),
                           today_len=len(list_today),
                           today_href = list_today_href)

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
                           today_len=len(list_today),
                           today_href = list_today_href)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
