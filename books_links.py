import requests
from bs4 import BeautifulSoup


url_cat = 'http://books.toscrape.com/catalogue/'

def books_links (url):
    links = []
    nextpage = ''
    while True:
        response=requests.get(url.replace('index.html','') + nextpage)
        if  response.ok:
            soup= BeautifulSoup(response.content, 'html.parser')
            link_block = soup.select('.image_container')
            for i in range(len(link_block)):
                links.append(url_cat + link_block[i].a['href'].replace('../', ''))   
        if  response.text.find('<li class="next">') != -1:
            nextpage = soup.select_one(".next").a['href']
        else:
            break
    return links


    