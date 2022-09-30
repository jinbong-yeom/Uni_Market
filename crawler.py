from bs4 import BeautifulSoup
import requests
import time


#당근마켓 검색
def daangn_search(search_word):
    daangn_data = {'picture': [],
            'title': [],
            'Region': [],
            'Price': [],
            'Link': []}

    for n in range(1, 5):
        url = 'https://www.daangn.com/search/{}/more/flea_market?page={}'.format(search_word, n)

        r = requests.get(url)

        soup = BeautifulSoup(r.text, 'html.parser')

        contents = soup.find_all('article', class_ = "flea-market-article flat-card")

        for i in contents:
            title = i.find("span")
            picture = i.find("img")
            img_src = picture.get("src")
            region = i.find('p', class_ = "article-region-name")
            price = i.find('p', class_ = "article-price")
            link = 'https://www.daangn.com' + i.find('a')['href']

            daangn_data['title'].append(title.text.strip())
            daangn_data['picture'].append(img_src)
            daangn_data['Region'].append(region.text.strip())
            daangn_data['Price'].append(price.text.strip())
            daangn_data['Link'].append(link)
        
        print(daangn_data)


#번개장터 검색
def bunjang_search(search_word):
    bunjang_data = {
            'title': [],
            'picture': [],
            'Region': [],
            'Price': [],
            'Link': []}

    url = 'https://api.bunjang.co.kr/api/1/find_v2.json?q={}'.format(search_word)

    r = requests.get(url)

    contents = r.json().get("list")
    for i in contents:
        title = i.get("name")
        picture = i.get("product_img")
        region = i.get("location")
        price = i.get("price")
        link = 'https://m.bunjang.co.kr/products/' + i.get("pid")

        bunjang_data['title'].append(title)
        bunjang_data['picture'].append(picture)
        bunjang_data['Region'].append(region)
        bunjang_data['Price'].append(price)
        bunjang_data['Link'].append(link)


    print(bunjang_data)

daangn_search("노트북")

bunjang_search("노트북")
