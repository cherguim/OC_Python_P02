import requests
from bs4 import BeautifulSoup


def book_categories (url_base):
                
    categories_names = []  
    categories_links = []

    response=requests.get(url_base)
    if response.ok:
        
        soup= BeautifulSoup(response.content, 'html.parser')
    
        category_block = soup.select(".nav-list > li > ul > li ")

        for i in range(len(category_block)):
            categories_names.append (category_block[i].select_one("a").text.strip().replace(' ', '_'))
            categories_links.append (url_base + category_block[i].a['href'].replace("../", ""))
        
          
    return categories_names, categories_links      
    


    