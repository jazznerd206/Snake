import schedule, time
import requests
from bs4 import BeautifulSoup


def stock_price(symbol):
    url = "https://in.finance.yahoo.com/quote/" + symbol + "?s=" + symbol + '"'
    print('finding...')
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    class_ = "My(6px) Pos(r) smartphone_Mt(6px)"
    return soup.find("div", class_=class_).find("span").text

def job(ticker):
    print(stock_price(ticker))

ticker = input('ticker: ')
job(ticker)
time.sleep(1)
hourly = []