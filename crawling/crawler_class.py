from crawler_module import Crawler
import requests
from bs4 import BeautifulSoup

class Danngn(Crawler):
    
    crawler_data = []

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
    



class Bunjang(Crawler):
    crawler_data = []

    def crawler_search(self, search_word):
    
        url = 'https://api.bunjang.co.kr/api/1/find_v2.json?q={}'.format(search_word)

        r = requests.get(url)

        
        contents = r.json().get("list")
        for i in contents:
            item_id = i.get("pid")
            title = i.get("name")
            picture = i.get("product_image")
            region = i.get("location")
            price = i.get("price")
            link = 'https://m.bunjang.co.kr/products/' + item_id

            tmp = [item_id, title, picture, region, price, link]

            self.crawler_data.append(tmp)
