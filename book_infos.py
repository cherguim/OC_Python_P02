import requests
from bs4 import BeautifulSoup
import book_transform as trans
import sys
pmain = sys.modules['__main__']

def book_infos (urls):

    rows = [['product_page_url', 'universal_product_code', 'title',
         'price_including_tax (GBP)', 'price_excluding_tax (GBP)', 
         'number_available', 'product_description', 'category', 
         'review_rating (max 5)', 'image_url']]

    print('\n' + f"{'Status':20}{rows[0][7]:22}{rows[0][2]:10}" + '\n' )
    for url in urls:
        response=requests.get(url)
        if response.ok:
            soup= BeautifulSoup(response.content, 'html.parser')
            product_page_url = url
            universal_product_code = soup.select_one("table > tr > td").text
            title = soup.select_one("h1").text
            price_including_tax =soup.select("table > tr")[3].select_one("td").text.replace('£','')
            price_including_tax = trans.t_money (price_including_tax,rows)
            price_excluding_tax = soup.select("table > tr")[2].select_one("td").text.replace('£','')
            price_excluding_tax = trans.t_money (price_excluding_tax, rows)
            number_available = soup.select("table > tr")[5].select_one("td").text
            number_available = number_available.replace('In stock (', '').replace(' available)','')
            try:
                product_description = soup.select_one(".sub-header + p").text
            except AttributeError as err:
                product_description =''
                # save url and err to error_log.txt   
            category = soup.select(".breadcrumb > li")[2].select_one("a").text
            review_rating = trans.t_rating(soup.select_one(".star-rating")["class"][1])
            image_url = soup.select_one(".item > img")
            image_url = pmain.url_base + "/" + image_url["src"].replace("../", "")
                
            rows.append ([product_page_url, universal_product_code, title, 
                            price_including_tax, price_excluding_tax, 
                            number_available, product_description, category, 
                            review_rating, image_url])                

            print(f"{'Data scraping':20}{category:22}{pmain.lstr_80(title,70):10}")

    return rows
