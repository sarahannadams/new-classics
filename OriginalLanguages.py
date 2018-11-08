import json, csv, re

#opening the json file with the information from each book page
book_info = json.load(open("new_classics_book_info.json", "r"))

#setting up a list 
language_list = []

count=0

def language_pull_clean(input):

	input = str(input)
	input = input.strip("[' ']")
	
	return input 

for orig_language in book_info:

	find_language = re.compile("(?<=from the) [A-Z][a-z]+")
	orig_language = find_language.findall(str(book_info))
	orig_language = language_pull_clean(orig_language)

	if find_language == re.compile("(?<=from the) [A-Z][a-z]+"):
		language = orig_language
	
	else:
		language = "English"
	
	count= count + 1
		
	orig_language_info = {}
	
	orig_language_info["id"] = count
	orig_language_info["original_language"] = language
	
	language_list.append(orig_language_info)
	
json.dump(language_list, open("language_list.json", "w"), indent=2)
	
	

