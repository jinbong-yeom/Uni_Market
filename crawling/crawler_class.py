from crawler_module import Crawler
from bs4 import BeautifulSoup
import requests
import datetime


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


class Joongna(Crawler):
    crawler_data = []

    def crawler_search(self, search_word):
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
            'searchWord': "{}".format(search_word),
            'osType': 2,
        }

        response = requests.post('https://search-api.joongna.com/v25/list/category', headers=headers, json=json_data)

        contents = response.json().get("data").get("items")
        
        for i in contents:
            print(i)
            item_id = str(i.get("seq"))
            title = i.get("title")
            picture = i.get("detailImgUrl")
            region = i.get("locationNames")
            price = i.get("price")
            link = 'https://web.joongna.com/product/detail/' + item_id


            tmp = [item_id, title, picture, region, price, link]

            self.crawler_data.append(tmp)