import csv, json

#opening json file for reading and assigning variable
subtitles_parsed = json.load(open("new_classics_book_info.json", "r", encoding="utf-8"))

#opening new csv file for writing into
subtitle_csv = open("16_subtitles.csv", "w", encoding="utf-8")

#employing csv.writer function
csvwriter = csv.writer(subtitle_csv)

#setting up count for the rows
count = 0

#looping through our book entries
for subtitle in subtitles_parsed:
 	
 	#if it is the first row they are headers (keys from our JSON dictionaries)
 	if count == 0:
 	
 		header = subtitle.keys()
 		
 		csvwriter.writerow(header)
 		
 		#if the count is greater than 1 those are rows (values from our JSON dictionaries)
 		count += 1
 		
 	csvwriter.writerow(subtitle.values())

#closing our new csv file 	
subtitle_csv.close()