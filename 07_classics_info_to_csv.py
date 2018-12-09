import csv, json

#opening json file for reading and assigning variable
book_info_parsed = json.load(open("new_classics_book_info.json", "r", encoding="utf-8"))

#opening new csv file for writing into
book_info = open("08_classics_info.csv", "w", encoding="utf-8")

#employing csv.writer function
csvwriter = csv.writer(book_info)

#setting up count for the rows
count = 0

#looping through our book entries
for book_element in book_info_parsed:
 	
 	#if it is the first row they are headers (keys from our JSON dictionaries)
 	if count == 0:
 	
 		header = book_element.keys()
 		
 		csvwriter.writerow(header)
 		
 		#if the count is greater than 1 those are rows (values from our JSON dictionaries)
 		count += 1
 		
 	csvwriter.writerow(book_element.values())

#closing our new csv file 	
book_info.close()