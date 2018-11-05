import json, csv, re

book_info = json.load(open("new_classics_book_info.json", "r"))

def language_pull_clean(input):

	input = str(input)
	input = input.strip("[' ']")
	
	return input 

for orig_language in book_info:

	find_language = re.compile("(?<=from the) [A-Z][a-z]+")
	orig_language = find_language.findall(str(book_info))
	orig_language = language_pull_clean(orig_language)	
	
	print(orig_language)






#orig_languages = ("orig_languages.csv", "w")