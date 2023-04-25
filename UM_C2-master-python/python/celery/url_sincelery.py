import requests
import time

def func(urls):
    start = time.time()
    for url in urls:
        resp = requests.get(url)
        print(" %d (%s)" % (resp.status_code, url))
    print("It took", time.time() - start, "seconds")

if __name__ == "__main__":
    func(["http://duckduckgo.com", "https://juncotic.com", "https://mstdn.io", "https://diasp.eu", "https://startpage.com"])
