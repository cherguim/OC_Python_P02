import csv, os
from urllib.request import urlretrieve
# import datetime

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
                print('Save to file        ', row[7] ,'            ', row[2])
            nb+=1
        print('\n' + str(nb-1) ,' BOOKS SUCCESSFULLY IMPORTED IN: ',csv_file, '\n' )


