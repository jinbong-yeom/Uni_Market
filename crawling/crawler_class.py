from crawler_module import Crawler
from bs4 import BeautifulSoup
import requests
from datetime import datetime,timedelta
import re
import json


class Danngn(Crawler):
    app_name = "당근"
    crawler_data = []
    max_item_id = 0

    def crawler_search(self):
        self.crawler_data = []

        url = 'https://www.daangn.com/search/{}/more/flea_market?page={}'.format("청주", 1)

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
            detail_list = self.detail_page(link)
            description = detail_list[0]
            date = detail_list[1]
            seller_info = detail_list[2]
            tmp = [item_id, title, picture, region, price, link, description, date, seller_info, self.app_name]
            self.crawler_data.append(tmp)

            self.max_item_id = item_id

    def detail_page(self, link):
        r = requests.get(link)

        soup = BeautifulSoup(r.text, 'html.parser')
        try:
            description = soup.find('div', id='article-detail').find('p')
            description=re.sub('<.+?>', '', str(description), 0).strip()

        except(AttributeError):
            description = " "

        time = soup.find('time').text.strip()

        if '일' in time:
            time = int(re.sub(r'[^0-9]', '', time))
            date = datetime.today() - timedelta(time)
            date = date.strftime("%Y-%m-%d")

        elif '시간' in time:
            time = int(re.sub(r'[^0-9]', '', time))
            date = datetime.today() - timedelta(hours=time)
            date = date.strftime("%Y-%m-%d")
            
        elif '분' in time:
            time = int(re.sub(r'[^0-9]', '', time))
            date = datetime.today() - timedelta(minutes=time)
            date = date.strftime("%Y-%m-%d")


        seller_info = soup.find('dd')
        seller_info = re.sub('<.+?>', '', str(seller_info), 0).strip()
        seller_info = re.sub(r"\s+",'',str(seller_info), 0)

        detail_list = [description, date, seller_info]
        return detail_list

        
    



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
            detail_list = self.detail_page(item_id)
            description = detail_list[0]
            date = detail_list[1]
            seller_info = detail_list[2]
            tmp = [item_id, title, picture, region, price, link, description, date, seller_info, self.app_name]

            self.crawler_data.append(tmp)
            self.max_last_id = item_id

    def detail_page(self, item_id):
        r = requests.get('https://api.bunjang.co.kr/api/pms/v1/products-detail/{}?viewerUid=-1'.format(item_id))

        contents = r.json().get("data")
        product = contents.get("product")
        
        date = product.get("updatedAt")
        temp = date.find('T')
        date = date[:temp]
        
        description = product.get("description")
        
        seller_info = contents.get("shop").get("grade")
        
        detail_list = [description, date, seller_info]
        return detail_list



class Joongna(Crawler):
    crawler_data = []
    app_name = "중고"
    max_last_id = 0

    def crawler_search(self):
        self.crawler_data = []
        now = datetime.now().replace(microsecond=0)

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

            detail_list = self.detail_page(item_id)
            description = detail_list[0]
            date = detail_list[1]
            seller_info = detail_list[2]
            tmp = [item_id, title, picture, region, price, link, description, date, seller_info, self.app_name]

            self.crawler_data.append(tmp)
            self.max_last_id = item_id

    def detail_page(self, item_id):
        response = requests.post('https://web.joongna.com/product/{}'.format(item_id))

        response = BeautifulSoup(response.text, 'html.parser')

        json_parser = str(response.find("script", id='__NEXT_DATA__'))
        json_parser=re.sub('<.+?>', '', json_parser, 0).strip()

        json_parser = json.loads(json_parser)
        json_parser = json_parser['props']['pageProps']['dehydratedState']['queries'][0]['state']['data']['data']
        description = json_parser['productDescription']
        date = json_parser['sortDate']

        temp = date.find(' ')
        date = date[:temp]

        seller_info = json_parser['store']['levelName']
        detail_list = [description, date, seller_info]
        return detail_list
