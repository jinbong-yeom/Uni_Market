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


daangn_search("노트북")