import requests
from bs4 import BeautifulSoup


def book_categories (url):              
    cats = []
    response=requests.get(url)
    if response.ok:  
        soup= BeautifulSoup(response.content, 'html.parser')
        cat_block = soup.select(".nav-list > li > ul > li ")
        for i in range(len(cat_block)):
            names = (cat_block[i].select_one("a").text.strip().replace(' ', '_'))
            links = (url + cat_block[i].a['href'].replace("../", ""))
            cats.append([names,links])
    return cats     


    