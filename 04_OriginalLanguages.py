import json, csv, re

#opening the json file with the information from each book page
book_info = json.load(open("new_classics_book_info.json", "r"))

#setting up a list from which I am going to form my JSON (list of dictionaries later)
language_list = []

#setting up count which will be the ID later
count=0

#function which makes sure the language pulled from the json comes out clean
def language_pull_clean(input):

	input = str(input)
	pattern = re.compile("<re.Match object; span=\([0-9]+, [0-9]+\), match=' ")
	match = pattern.findall(str(input))
	input = input.strip(str(match))
	pattern = re.compile("'>")
	match = pattern.findall(str(input))
	input = input.strip(str(match))
	
	return input 

#looping through the json to find original languages
for orig_language in book_info:

	#implementing the regex
	find_language = re.compile("(?<=from the) [A-Z][a-z]+")
	orig_language = find_language.search(str(orig_language))
	
	#using function so that we get a language without any extra stuff
	orig_language = language_pull_clean(orig_language)
	
	#adding a count after each loop to give each language the proper id	
	count= count + 1
	
	#if statement to replace "None" string with appropriate language where regex didn't pick it up	
	if orig_language == "None" and count == 184:
		orig_language = "Russian"
	if orig_language == "None" and count == 346:
		orig_language = "Chinese"
	if orig_language == "None" and count == 337:
		orig_language = "Various"	
	if orig_language == "None" and count == 250:
		orig_language= "Italian"
	elif orig_language == "None":
		orig_language= "English"		
	
	#setting up dictionary for json file	
	orig_language_info = {}
	
	#defining keys and values in dictionary
	orig_language_info["id"] = count
	orig_language_info["original_language"] = orig_language
	
	#appending our dictionaries to the list
	language_list.append(orig_language_info)

#dumping our list of dictionaries into a json file	
json.dump(language_list, open("language_list.json", "w"), indent=2)



	
	


	

