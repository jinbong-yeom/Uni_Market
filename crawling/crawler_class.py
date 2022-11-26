from crawler_module import Crawler
from bs4 import BeautifulSoup
import requests
import datetime
import re


class Danngn(Crawler):
    app_name = "당근"
    crawler_data = []
    max_item_id = 0

    def crawler_search(self, region_keyword):
        self.crawler_data = []

        url = 'https://www.daangn.com/search/{}/more/flea_market?page={}'.format(region_keyword, 1)

        r = requests.get(url)

        soup = BeautifulSoup(r.text, 'html.parser')

        contents = soup.find_all('article', class_ = "flea-market-article flat-card")

        for i in contents:
            item_id = i.find('a')['href']
            item_id = int(re.sub(r"[^0-9]", "", item_id))
            if self.max_item_id >= item_id:
                continue
            title = i.find("span").text.strip()

            picture = i.find("img").get("src")
            region = i.find('p', class_ = "article-region-name").text.strip()
            price = i.find('p', class_ = "article-price").text.strip()
            price = self.price_filtering(price)
            if price == -1:
                continue
            link = 'https://www.daangn.com/articles/' + str(item_id)
            #time = self.renewal_time(link)
            tmp = [item_id, title, picture, region, price, link, self.app_name]
            self.crawler_data.append(tmp)

            self.max_item_id = item_id

    def renewal_time(self, link):
        r = requests.get(link)

        soup = BeautifulSoup(r.text, 'html.parser')

        time = soup.find('time').text.strip()

        time = re.sub(r'[^0-9]', '', time)

        
    



class Bunjang(Crawler):

    app_name = "번개"
    crawler_data = []
    max_last_id = 0

    def crawler_search(self):
        self.crawler_data = []
        url = 'https://api.bunjang.co.kr/api/1/find_v2.json?q={}'

        r = requests.get(url)

        
        contents = r.json().get("list")
        for i in contents:
            item_id = int(i.get("pid"))
            if self.max_last_id >= item_id:
                continue
            title = i.get("name")
            
            picture = i.get("product_image")
            region = i.get("location")
            price = i.get("price")
            price = self.price_filtering(price)
            if price == -1:
                    continue
            link = 'https://m.bunjang.co.kr/products/' + str(item_id)
            
            tmp = [item_id, title, picture, region, price, link, self.app_name]

            self.crawler_data.append(tmp)
            self.max_last_id = item_id
    


class Joongna(Crawler):
    crawler_data = []
    app_name = "중고"
    max_last_id = 0

    def crawler_search(self):
        self.crawler_data = []
        now = datetime.datetime.now().replace(microsecond=0)

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'App-Version': 'null',
            'Connection': 'keep-alive',
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
            'Origin': 'https://web.joongna.com',
            'Os-Type': '2',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }

        json_data = {
            'startIndex': 0,
            'searchStartTime': str(now),
            'filter': {
                'maxPrice': 2000000000,
                'minPrice': 0,
                'categoryDepth': 0,
                'categorySeq': 0,
            },
            'searchQuantity': 20,
            'categoryName1': '',
            'categoryName2': '',
            'categoryName3': '',
            'quantity': 20,
            'firstQuantity': 20,
            'searchWord': '',
            'osType': 2,
        }

        response = requests.post('https://search-api.joongna.com/v25/list/category', headers=headers, json=json_data)

        contents = response.json().get("data").get("items")
        
        for i in contents:
            item_id = int(i.get("seq"))
            if self.max_last_id >= item_id:
                continue
            title = i.get("title")

            picture = i.get("detailImgUrl")
            region = i.get("locationNames")
            price = i.get("price")
            price = self.price_filtering(str(price))
            if price == -1:
                continue
            link = 'https://web.joongna.com/product/detail/' + str(item_id)


            tmp = [item_id, title, picture, region, price, link, self.app_name]

            self.crawler_data.append(tmp)
            self.max_last_id = item_id
