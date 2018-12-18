import json

#setting up list for dictionary
book_list = []



#opening json file to loop through it to pull out what I want
book_titles = json.load(open('02_classics.json'))

#looping through and assigning variables to what I want
for book_item in book_titles:
	book_id = book_item['id']
	title = book_item['title']
	book_page_url = book_item['book_page_url']
	image_url = book_item['image_url']
	
	#setting up dictionary
	combined_data = {}	

	#assigning keys and values for the new dictionary	
	combined_data['book_id'] = book_id
	combined_data['title'] = title
	combined_data['book_page_url'] = book_page_url
	combined_data['image_url'] = image_url	
	
	book_list.append(combined_data)
	
# opening json file to loop through it to pull out what I want	
authors = json.load(open('19_author_geospatial_data.json'))

# looping through and assigning variables to what I want
for author_item in authors['rows']:
	book_id = author_item['Book ID']
	nyrb_author_name = author_item['web_scrape_name']
	wikidata_author_name = author_item['openrefine_author_name']
	wikidata_q_id = author_item['wikidata_q_id']
	place_of_birth_city = author_item['place_of_birth_city']
	place_of_birth_country = author_item['place_of_birth_country']
	place_of_birth_coordinate_location = author_item['place_of_birth_coordinate location']
	place_of_death_city = author_item['place_of_death_city']
	place_of_death_country = author_item['place_of_death_country']
	place_of_death_coordinate_location = author_item['place_of_death_coordinate_location']
	statelessness = author_item['statelessness']	
	
	#setting up dictionary
	combined_data = {}	

	# 	assigning keys and values for the new dictionary
	combined_data['book_id'] = book_id
	combined_data['nyrb_author_name'] = nyrb_author_name
	combined_data['wikidata_author_name'] = wikidata_author_name	
	combined_data['wikidata_q_id'] = wikidata_q_id
	combined_data['place_of_birth_city'] = place_of_birth_city
	combined_data['place_of_birth_country'] = place_of_birth_country
	combined_data['place_of_birth_coordinate_location'] = place_of_birth_coordinate_location
	combined_data['place_of_death_city'] = place_of_death_city
	combined_data['place_of_death_country'] = place_of_death_country
	combined_data['place_of_death_coordinate_location'] = place_of_death_coordinate_location
	combined_data['statelessness'] = statelessness  
	
	book_list.append(combined_data)
	
# opening json file to loop through it to pull out what I want	
subtitles = json.load(open('14_subtitles.json'))

# looping through and assigning variables to what I want
for subtitle_item in subtitles:	
	book_id = subtitle_item['id']
	subtitle = subtitle_item['subtitle']
	
	#setting up dictionary
	combined_data = {}	

	# 	assigning keys and values for the new dictionary
	combined_data['book_id'] = book_id
	combined_data['subtitle'] = subtitle	
	
	book_list.append(combined_data)
	
# opening json file to loop through it to pull out what I want	
languages = json.load(open('10_language_list.json'))

# looping through and assigning variables to what I want
for lang_item in languages:
	book_id = lang_item['id']
	original_language = lang_item['original_language']
	
	#setting up dictionary
	combined_data = {}	

	# 	assigning keys and values for the new dictionary
	combined_data['book_id'] = book_id
	combined_data['original_language'] = original_language	
	
	book_list.append(combined_data)
	
# opening json file to loop through it to pull out what I want
book_info = json.load(open('06_classics_info.json'))

# looping through and assigning variables to what I want
for info_item in book_info:
	book_id = info_item['id']
	isbn = info_item['isbn']
	pub_date = info_item['pub_date']
	
	#setting up dictionary
	combined_data = {}	

	# 	assigning keys and values for the new dictionary
	combined_data['book_id'] = book_id
	combined_data['isbn'] = isbn
	combined_data['nyrb_pub_date'] = pub_date
	
	book_list.append(combined_data)


	
	# appending dictionary to list of books	
# 	book_list.append(combined_data['book_id'])
# 	book_list.append(combined_data['title'])
# 	book_list.append(combined_data['book_page_url'])
# 	book_list.append(combined_data['image_url'])
# 		appending dictionary to list of books	
# 	book_list.append(combined_data['nyrb_author_name'])	
# 	book_list.append(combined_data['wikidata_author_name'])
# 	book_list.append(combined_data['wikidata_q_id'])
# 	book_list.append(combined_data['place_of_birth_city'])
# 	book_list.append(combined_data['place_of_birth_country'])
# 	book_list.append(combined_data['place_of_birth_coordinate_location'])
# 	book_list.append(combined_data['place_of_death_city'])
# 	book_list.append(combined_data['place_of_death_country'])
# 	book_list.append(combined_data['place_of_death_coordinate_location'])
# 	book_list.append(combined_data['statelessness'])
# 		appending dictionary to list of books	
# 	book_list.append(combined_data['subtitle'])
# 		appending dictionary to list of books	
# 	book_list.append(combined_data['original_language'])	
# 		appending dictionary to list of books	
# 	book_list.append(combined_data['isbn'])	
# 	book_list.append(combined_data['nyrb_pub_date'])
	
	
# putting this into a new json file 	
json.dump(book_list, open("allData_NewClassics.json", "w"), indent=2)

	
#this is Matt's template that he sent us
# combined_data = {}
# 
# file1 = json.load(open('whatever.json'))
# 
# combined_data['something'] = file1['data']
# 
# file2 = json.load(open('whatever2.json'))
# 
# combined_data['something_else'] = file2['data']
# 
# etc..
# 
# json.dump(open('newfile.json','w'))












