import json, csv, re

#opening the json file with the information from each book page
book_info = json.load(open("new_classics_book_info.json", "r"))

#setting up a list from which I am going to form my JSON (list of dictionaries later)
author_list = []

#setting up count which will be the ID later
count=0

#looping through the json to find authors
for combined_authors in book_info:

	#implementing the regex
	find_author = re.compile("")
	author = find_author.findall(combined_authors)		
	
	#adding a count after each loop to give each language the proper id	
	count= count + 1
	
	#setting up dictionary for json file	
	orig_language_info = {}
	
	#defining keys and values in dictionary
	author_info["id"] = count
	author_info["author"] = orig_language
	
	#appending our dictionaries to the list
	author_list.append(author_info)

#dumping our list of dictionaries into a json file	
json.dump(author_list, open("authors.json", "w"), indent=2)