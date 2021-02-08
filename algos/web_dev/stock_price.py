import schedule, time
import requests
from bs4 import BeautifulSoup


def stock_price(symbol):
    url = "https://in.finance.yahoo.com/quote/" + symbol + "?s=" + symbol + '"'
    print('finding...')
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    # print(soup)
    class_ = "My(6px) Pos(r) smartphone_Mt(6px)"
    return soup.find("div", class_=class_).find("span").text

def job(ticker):
    return stock_price(ticker)
    time.sleep(1)

# def ez_job():
#     print('test job')

# print('ARKG', stock_price("ARKG"))
# print('SPCE', stock_price("SPCE"))
# print('NOK', stock_price("NOK"))

if __name__ == '__main__':
    ticker = input('ticker: ')
    while True:
        job(ticker)
    