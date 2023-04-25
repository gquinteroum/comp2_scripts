import concurrent.futures
import urllib.request

URLS = [
        'http://www.losandes.com.ar/',
        'http://kernel.org/',
        'http://debian.org/',
        'http://juncotic.com/']

# Retrieve a single page and report the url and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def main1():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # armamos un diccionario con la url y el objeto executor de cada una
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))

def main2():
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)

    future_to_url = {}
    for url in URLS:
        # armamos un diccionario con la url y el objeto executor de cada una
        future_to_url.update({executor.submit(load_url, url, 60):url})


    for future in concurrent.futures.as_completed(future_to_url):
        print("%s : %d" % (future_to_url[future],len(future.result())))


main1()
print("main2-----------------------------------")
main2()


"""
as_completed()
    toma un iterable de objetos Future
    va devolviendo los valores en la medida en que se van calculando
"""
