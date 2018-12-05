import csv, json

#opening json file for reading and assigning variable
languages_parsed = json.load(open("language_list.json", "r", encoding="utf-8"))

#opening new csv file for writing into
languages = open("language_list.csv", "w", encoding="utf-8")

#employing csv.writer function
csvwriter = csv.writer(languages)

#setting up count for the rows
count = 0

#looping through our book entries
for lang_element in languages_parsed:
 	
 	#if it is the first row they are headers (keys from our JSON dictionaries)
 	if count == 0:
 	
 		header = lang_element.keys()
 		
 		csvwriter.writerow(header)
 		
 		#if the count is greater than 1 those are rows (values from our JSON dictionaries)
 		count += 1
 		
 	csvwriter.writerow(lang_element.values())

#closing our new csv file 	
languages.close()