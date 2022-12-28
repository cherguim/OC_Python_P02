import requests
from bs4 import BeautifulSoup

url_base = 'http://books.toscrape.com'



def book_infos (urls):
    rows = [['product_page_url', 'universal_product_code', 'title',
                            'price_including_tax (£)', 'price_excluding_tax (£)', 
                            'number_available', 'product_description', 'category', 
                            'review_rating', 'image_url']]
    
    # A faire: formatage des espacements 
    print ('\nStatus              ',    rows[0][7] ,'          ', rows[0][2], '\n')  
    for url in urls:
        response=requests.get(url)
        if response.ok:
            soup= BeautifulSoup(response.content, 'html.parser')
            product_page_url = url
            universal_product_code = soup.select_one("table > tr > td").text
            title = soup.select_one("h1").text
            price_including_tax = soup.select("table > tr")[3].select_one("td").text.replace('£','')
            price_excluding_tax = soup.select("table > tr")[2].select_one("td").text.replace('£','')
            number_available = soup.select("table > tr")[5].select_one("td").text
            number_available = number_available.replace('In stock (', '').replace(' available)','')
            try:
                product_description = soup.select_one(".sub-header + p").text
            except AttributeError as err:
                product_description =''
                # save url and err to error_log.txt   
            category = soup.select(".breadcrumb > li")[2].select_one("a").text
            review_rating = soup.select("table > tr")[6].select_one("td").text
            image_url = soup.select_one(".item > img")
            image_url = url_base + "/" + image_url["src"].replace("../", "")
                
            rows.append ([product_page_url, universal_product_code, title, 
                            price_including_tax, price_excluding_tax, 
                            number_available, product_description, category, 
                            review_rating, image_url])                
            # A faire: formatage des espacements
            print ('Data scraping       ',        category ,'            ', title)

    return rows
