from book_infos import book_infos
from book_categories import book_categories
from book_save import book_save
from books_links import books_links
import requests, platform, os

url_base = 'http://books.toscrape.com/'
save_base = 'output'
book_csv = save_base + '/_scrape_one_book.csv'


def scrape_one_book(url):
    if url.find(url_base) !=-1:
        response=requests.get(url)
        # network connection error:
        # socket.gaierror: [Errno 8] nodename nor servname provided, or not know
        if response.ok:
            if response.text.find('class="product_page"') !=-1:
                links=[]
                links.append(url)
                rows = book_infos(links)
                book_save(book_csv, rows)
            else: 
                print ('\n \n Bad url, choose a URL for a single book with its product description!')
    else:
        print ('\n Bad url, chose only one book from "http://books.toscrape.com" web site')


def scrape_one_category():
    cats = book_categories(url_base)
    while True:
        clear_screen()
        i=0
        for name, link in cats:
            i +=1
            print(str(i).rjust(2), '-' , name)
        print ('\nSelect one category between 1 and',i,':')
        ans = input('->')
        if ans.isdigit():
            ans = (int(ans))
            if ans <= len(cats) and ans !=0:
                links = books_links(cats[ans-1][1])
                rows = book_infos(links)
                book_save('output/' + rows[1][7] + '.csv', rows)
                break
               

def scrape_all_categories ():
    cats = book_categories (url_base)
    for cat in cats:
        links = books_links (cat[1])
        rows = book_infos(links)
        book_save('output/' + rows[1][7] + '.csv', rows)  


def lstr_80(txt,nb):
    if (len(txt))>nb:
        txt = (txt[:nb]+' ...')
    return txt


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Darwin" or "Linux":
        os.system("clear")


while True:
    clear_screen()
    print('Data scraping of "http://books.toscrape.com" web site\n')
    print('1 - Data scraping for only one book')
    print('2 - Data scraping for one category of books')
    print('3 - Data scraping for all category of books')
    print('4 - Quit')
    print('\nYour choice ? ')
    answer = input('-> ')
    print()

    if answer == '1':
        print('Please enter the url to scrape data for a single book:')
        answer = input('-> ')
        scrape_one_book(answer)
        input('\nPress a key to continue. ')

    if answer == '2':
        scrape_one_category()
        input('\nPress a key to continue. ')
    if answer == '3':
        scrape_all_categories()
        input('\nPress a key to continue. ')  

    if answer in ('4', 'q', 'Q'):   
        quit()

