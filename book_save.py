import csv, os
from urllib.request import urlretrieve
# import datetime#
import sys
pmain = sys.modules['__main__']

def book_save(csv_file, rows):
    img_dir = csv_file.rsplit("/", 1)[:-1][0] + '/_img/'
    if not os.path.exists(img_dir):     
        os.makedirs(img_dir)
    with open(csv_file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        nb=0
        for row in rows:
            csvwriter.writerow(row) 
            if nb>0:    
                # Avoid saving an image if it already exists for saving time
                if not os.path.exists(img_dir + row[1] + '.jpg'):      
                    urlretrieve(row[9], img_dir + row[1] + '.jpg')   
                print(f"{'Save to file':20}{row[7]:22}{pmain.lstr_80(row[2],70):10}")
            nb+=1
        print('\n' + str(nb-1) ,'book(s) writeen with success in this file:','"',csv_file,'"', '\n' )


