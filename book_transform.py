

import book_infos


def t_rating (val):
    # Convert literal rate to numeric
    rating_liste = ['', 'One', 'Two', 'Three', 'Four', 'Five' ]
    T_rating = str(rating_liste.index(val))
    return T_rating

"""
def t_money (price, rows):
    # Convert British Pound to US Dollar
    # Exchange rate -> 1 GBP = 1,20 USD 
    nb = price.replace('.','')   
    if nb.isdigit():
        rows[0][3] = rows[0][3].replace('GBP','USD')
        rows[0][4] = rows[0][3].replace('GBP','USD')
        price = f"{float(price) * 1.2:.2f}"
    return price
"""

def t_money (price, rows):
    # Convert British Pound to Euro
    # Exchange rate -> 1 GBP = 1,13 Euro 
    nb = price.replace('.','')   
    if nb.isdigit():
        rows[0][3] = rows[0][3].replace('GBP','Euro')
        rows[0][4] = rows[0][3].replace('GBP','Euro')
        price = f"{float(price) * 1.13:.2f}"
    return price
