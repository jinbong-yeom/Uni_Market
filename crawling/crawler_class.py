from crawling.crawler_module import Crawler
import requests
from bs4 import BeautifulSoup

class Danngn(Crawler):
    
    crawler_data = []

    def __init__(self):
        self.crawler_data = []

    def crawler_search(self, search_word):
        
        for n in range(1, 4):
            url = 'https://www.daangn.com/search/{}/more/flea_market?page={}'.format(search_word, n)

            r = requests.get(url)

            soup = BeautifulSoup(r.text, 'html.parser')

            contents = soup.find_all('article', class_ = "flea-market-article flat-card")

            for i in contents:
                item_id = i.find('a')['href']
                title = i.find("span").text.strip()
                picture = i.find("img").get("src")
                region = i.find('p', class_ = "article-region-name").text.strip()
                price = i.find('p', class_ = "article-price").text.strip()
                link = 'https://www.daangn.com' + item_id

                tmp = [item_id, title, picture, region, price, link]

                self.crawler_data.append(tmp)
    

    def find_all(self):
        for one in len(self.crawler_data):
            print("item_id:" + one[0] + "title:" + one[1] + "picture:"+one[2] + "region" + one[3] + "price:" + one[4] + "link:"+one[5])

    def find_one(self, item_id):
        for one in len(self.crawler_data):
            if one[0] == item_id:
                return one
            else:
                return 

    def data_clean(self):
        self.crawler_data = []
    
