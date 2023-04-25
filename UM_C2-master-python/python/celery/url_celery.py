import requests, time
from celery import Celery

#app = Celery('url_celery', broker='redis://localhost:6379/0', backend='redis://localhost:6379')
app = Celery('url_celery', broker='redis://analytics.juncotic.com:6379/0', backend='redis://analytics.juncotic.com:6379')

@app.task
def fetch_url(url):
    resp = requests.get(url)
    print(" %d (%s)" % (resp.status_code, url))
    return " %d (%s)" % (resp.status_code, url)

def func(urls):
    for url in urls:
        fetch_url.delay(url)

if __name__ == "__main__":
    func(["http://duckduckgo.com", "https://juncotic.com", "https://mstdn.io", "https://diasp.eu", "https://startpage.com"])
