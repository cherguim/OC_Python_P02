import requests
from bs4 import BeautifulSoup


url_catalogue = 'http://books.toscrape.com/catalogue/'


def books_links (url_category):
    links = []
    nextpage = ''
    
    while True:
        response=requests.get(url_category + nextpage)
        
        if  response.ok:
            soup= BeautifulSoup(response.content, 'html.parser')
            liens = soup.select(".image_container")
            
            for i in range(len(liens)):
                links.append(url_catalogue + liens[i].a['href'].replace("../", "")) 
                       
        if  response.text.find('<li class="next">') != -1:
            nextpage = soup.select_one(".next").a['href']

        else:
            break
        
    return links
