import csv


def book_csv (csv_file, Book_fields, Book_rows):
    with open(csv_file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(Book_fields) 
        csvwriter.writerow(Book_rows)
        
    

