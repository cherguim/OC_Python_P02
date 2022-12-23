from book_infos import book_infos
from book_categories import book_categories
from book_csv import book_csv
from books_links import books_links



# scrape d'un livre
url_book = 'http://books.toscrape.com/catalogue/wall-and-piece_971/index.html'
csv_file = 'output/book_infos.csv'
book_infos = book_infos (url_book)
book_csv (csv_file, book_infos[0], book_infos[1])

"""

#  scrape d'une catégorie
url_category = 'http://books.toscrape.com/catalogue/category/books/mystery_3/'
csv_file = 'output/mystery_3.csv'
 

#  scrape de toutes les catégories
url_base = 'http://books.toscrape.com/'

"""