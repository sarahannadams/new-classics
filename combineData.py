import json

# book_list = []

combined_data = {}

book_titles = json.load(open('02_classics.json', 'r'))


# book = 1
# 
# while book <= 515:

for item in book_titles:
	book_id = item['id']
	title = item['title']
	book_page_url = item['book_page_url']
	image_url = item['image_url']
	
authors = json.load(open('19_author_geospatial_data.json', 'r'))

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
	
languages = json.load(open('10_language_list.json'))

for item in languages:
	original_language = item['original_language']
	

book_info = json.load(open('06_classics_info.json', 'r'))

for item in book_info:
	isbn = item['isbn']
	pub_date = item['pub_date']
	
	
subtitles = json.load(open('14_subtitles.json', 'r'))

for item in subtitles:	
	subtitle = item['subtitle']
	
	

	
						
	# book = book+1



combined_data['book_id'] = book_id
combined_data['title'] = title
combined_data['subtitle'] = subtitle
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


# combined_data['nyrb_author_name'] = {}
# for element in combined_data['nyrb_author_name']:



combined_data['original_language'] = original_language
combined_data['book_page_url'] = book_page_url
combined_data['image_url'] = image_url
combined_data['isbn'] = isbn
combined_data['nyrb_pub_date'] = pub_date

					
	
# 	book_list.append(combined_data)


with open('allData_NewClassics.json', 'w') as out_file:
	json.dump(combined_data, out_file, indent=2)
	





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











