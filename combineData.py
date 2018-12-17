import json


#setting up dictionary
combined_data = {}

#opening json file to loop through it to pull out what I want
book_titles = json.load(open('02_classics.json'))

#looping through and assigning variables to what I want
for item in book_titles:
	book_id = item['id']
	title = item['title']
	book_page_url = item['book_page_url']
	image_url = item['image_url']

	#assigning keys and values for the new dictionary	
	combined_data['book_id'] = book_id
	combined_data['title'] = title
	combined_data['book_page_url'] = book_page_url
	combined_data['image_url'] = image_url
	
	
#opening json file to loop through it to pull out what I want	
authors = json.load(open('19_author_geospatial_data.json'))

#looping through and assigning variables to what I want
for item in authors['rows']:
	nyrb_author_name = item['web_scrape_name']
	wikidata_author_name = item['openrefine_author_name']
	wikidata_q_id = item['wikidata_q_id']
	place_of_birth_city = item['place_of_birth_city']
	place_of_birth_country = item['place_of_birth_country']
	place_of_birth_coordinate_location = item['place_of_birth_coordinate location']
	place_of_death_city = item['place_of_death_city']
	place_of_death_country = item['place_of_death_country']
	place_of_death_coordinate_location = item['place_of_death_coordinate_location']
	statelessness = item['statelessness']	
	
	#assigning keys and values for the new dictionary
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
	
	
#opening json file to loop through it to pull out what I want	
subtitles = json.load(open('14_subtitles.json'))

#looping through and assigning variables to what I want
for item in subtitles:	
	subtitle = item['subtitle']
	
	#assigning keys and values for the new dictionary
	combined_data['subtitle'] = subtitle
	
	
#opening json file to loop through it to pull out what I want	
languages = json.load(open('10_language_list.json'))

#looping through and assigning variables to what I want
for item in languages:
	original_language = item['original_language']
	
	#assigning keys and values for the new dictionary
	combined_data['original_language'] = original_language	
	
	
#opening json file to loop through it to pull out what I want
book_info = json.load(open('06_classics_info.json'))

#looping through and assigning variables to what I want
for item in book_info:
	isbn = item['isbn']
	pub_date = item['pub_date']
	
	#assigning keys and values for the new dictionary
	combined_data['isbn'] = isbn
	combined_data['nyrb_pub_date'] = pub_date
	
	
	
with open('allData_NewClassics.json', 'w') as out_file:
	json.dump(combined_data, out_file, indent=2)

	
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











