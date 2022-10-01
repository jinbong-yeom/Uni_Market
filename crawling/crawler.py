from bs4 import BeautifulSoup
import requests
import datetime

from crawler_class import Bunjang, Danngn


#당근마켓 검색
danngn = Danngn()
danngn.crawler_search("노트북")
danngn.find_all()

#번개장터 검색
bunjang = Bunjang()
bunjang.crawler_search("노트북")
bunjang.find_all()

def joongna_search(search_word, input_time):
    joongna_data = {'picture': [],
            'title': [],
            'Region': [],
            'Price': [],
            'Link': []}

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
        'searchStartTime': str(input_time),
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
        title = i.get("title")
        picture = i.get("detailImgUrl")
        region = i.get("locationNames")
        price = i.get("price")
        link = 'https://web.joongna.com/product/detail/' + str(i.get("seq"))

        joongna_data['title'].append(title)
        joongna_data['picture'].append(picture)
        joongna_data['Region'].append(region)
        joongna_data['Price'].append(price)
        joongna_data['Link'].append(link)

    print(joongna_data)

now_day = datetime.datetime.now().replace(microsecond=0)

joongna_search("노트북", now_day)
