import requests
from bs4 import BeautifulSoup
from book_csv import book_csv

url_base = 'http://books.toscrape.com'


def book_infos (url_book):
    response=requests.get(url_book)
    if response.ok:
        soup= BeautifulSoup(response.content, 'html.parser')
        product_page_url = url_book
        universal_product_code = soup.select_one("table > tr > td").text
        title = soup.select_one("h1").text
        price_including_tax = soup.select("table > tr")[3].select_one("td").text.replace('£','')
        price_excluding_tax = soup.select("table > tr")[2].select_one("td").text.replace('£','')
        number_available = soup.select("table > tr")[5].select_one("td").text
        number_available = number_available.replace('In stock (', '').replace(' available)','')
        product_description = soup.select_one(".sub-header + p").text
        category = soup.select(".breadcrumb > li")[2].select_one("a").text
        review_rating = soup.select("table > tr")[6].select_one("td").text
        image_url = soup.select_one(".item > img")
        image_url = url_base + "/" + image_url["src"].replace("../", "")
        
        
        Book_fields = ['product_page_url', 'universal_product_code', 'title',
                        'price_including_tax (£)', 'price_excluding_tax (£)', 
                        'number_available', 'product_description', 'category', 
                        'review_rating', 'image_url']
            
        Book_rows = [product_page_url, universal_product_code, title, 
                        price_including_tax, price_excluding_tax, 
                        number_available, product_description, category, 
                        review_rating, image_url]   
                
                
        return Book_fields, Book_rows

