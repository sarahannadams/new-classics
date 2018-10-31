import csv, json

books_parsed = json.load(open("new_classics.json", encoding="utf-8", "r"))

books_data = open("new_classics.csv", encoding="utf-8", "w")

csvwriter = csv.writer(books_data)

count = 0

for book in books_parsed:
 	
 	if count == 0:
 	
 		header = book.keys()
 		
 		csvwriter.writerow(header)
 		
 		count += 1
 		
 	csvwriter.writerow(book.values())
 	
books_data.close()

#referred to http://blog.appliedinformaticsinc.com/how-to-parse-and-convert-json-to-csv-using-python/ for help