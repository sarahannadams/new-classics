import csv, json

#opening json file for reading and assigning variable
books_parsed = json.load(open("new_classics.json", "r", encoding="utf-8"))

#opening new csv file for writing into
books_data = open("new_classics.csv", "w", encoding="utf-8")

#employing csv.writer function
csvwriter = csv.writer(books_data)

#setting up count for the rows
count = 0

#looping through our book entries
for book in books_parsed:
 	
 	#if it is the first row they are headers (keys from our JSON dictionaries)
 	if count == 0:
 	
 		header = book.keys()
 		
 		csvwriter.writerow(header)
 		
 		#if the count is greater than 1 those are rows (values from our JSON dictionaries)
 		count += 1
 		
 	csvwriter.writerow(book.values())

#closing our new csv file 	
books_data.close()

#referred to http://blog.appliedinformaticsinc.com/how-to-parse-and-convert-json-to-csv-using-python/ for help