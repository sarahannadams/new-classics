import json

# count = 0
# 
book_list = []

combined_data = {}

book_titles = json.load(open('02_classics.json', 'r'))
languages = json.load(open('10_language_list.json'))
book_info = json.load(open('06_classics_info.json', 'r'))
subtitles = json.load(open('14_subtitles.json', 'r'))
authors = json.load(open('19_author_geospatial_data.json', 'r'))

for item in book_titles:
	book_id = item['id']
	title = item['title']
	book_page_url = item['book_page_url']
	image_url = item['image_url']

for item in languages:
	original_language = item['original_language']

for item in book_info:
	isbn = item['isbn']
	pub_date = item['pub_date']

for item in subtitles:	
	subtitle = item['subtitle']
	
for item in authors['rows']:
	nyrb_author_name = item['web_scrape_name']
	
combined_data['book_id'] = book_id
combined_data['title'] = title
combined_data['subtitle'] = subtitle
combined_data['nyrb_author_name'] = nyrb_author_name

	
combined_data['nyrb_author_name'] = {}
for element in combined_data['nyrb_author_name']:
	wikidata_author_name = element['openrefine_author_name']
	wikidata_q_id = element['wikidata_q_id']
	place_of_birth_city = element['place_of_birth_city']
	place_of_birth_country = element['place_of_birth_country']
	place_of_birth_coordinate_location = element['place_of_birth_coordinate location']
	place_of_death_city = element['place_of_death_city']
	place_of_death_country = element['place_of_death_country']
	place_of_death_coordinate_location = element['place_of_death_coordinate_location']
	statelessness = element['statelessness']

combined_data['nyrb_author_name']['wikidata_author_name'] = wikidata_author_name	
combined_data['nyrb_author_name']['wikidata_q_id'] = wikidata_q_id
combined_data['nyrb_author_name']['place_of_birth_city'] = place_of_birth_city
combined_data['nyrb_author_name']['place_of_birth_country'] = place_of_birth_country
combined_data['nyrb_author_name']['place_of_birth_coordinate_location'] = place_of_birth_coordinate_location
combined_data['nyrb_author_name']['place_of_death_city'] = place_of_death_city
combined_data['nyrb_author_name']['place_of_death_country'] = place_of_death_country
combined_data['nyrb_author_name']['place_of_death_coordinate_location'] = place_of_death_coordinate_location
combined_data['nyrb_author_name']['statelessness'] = statelessness  
combined_data['original_language'] = original_language
combined_data['book_page_url'] = book_page_url
combined_data['image_url'] = image_url
combined_data['isbn'] = isbn
combined_data['nyrb_pub_date'] = pub_date

	
book_list.append(combined_data)

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











# import json
# from functools import reduce
# from collections import defaultdict
# 
# # function to merge json files
# def merge(a, b, path=None):
# 	a = defaultdict(path)
# 	b = defaultdict(path)
# 	if path is None: path = []
# 	for key in b:
# 		if key in a:
# 			if isinstance(a[key], dict) and isinstance(b[key], dict):
# 				merge(a[key], b[key], path + [str(key)])
# 			elif a[key] == b[key]:
# 				# same value
# 				pass 
# 			else:
# 				raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
# 	else:
# 		a[key] = b[key]
# 	return a
# 
# with open('new_classics.json', 'r') as fp1:
# 	with open('subtitles.json', 'r') as fp2:		
# 		
# 		jsondata1=json.load(fp1)
# 		jsondata2=json.load(fp2)		
# 	
# with open('allData_NewClassics.json', 'w') as f:
# 	json.dump(merge(jsondata1,jsondata2, path=None),f,sort_keys=True)



#import json
# 
# def merge(a, b):
#     for key in b:
#     	# if key is in both a and b
#         if key in a:
#         	# if the key is dict Object
#             if isinstance(a[key], dict) and isinstance(b[key], dict): 
#                 merge(a[key], b[key])
#             else:
#               a[key] =a[key]+ b[key]
#         # if the key is not in dict a , add it to dict a      
#         else: 
#             a.update(b)
#     return a
# 
# all_data = []
# 
# with open('new_classics.json', 'r') as fp1:
# 	with open('subtitles.json', 'r') as fp2:		
# 		
# 		jsondata1=json.load(fp1)
# 		jsondata2=json.load(fp2)		
# 	
# with open('allData_NewClassics.json', 'w') as f:
# 	json.dump(merge(jsondata1,jsondata2),f,sort_keys=True,encoding='utf-8', ensure_ascii=False)
	



# allData_NewClassics = {}
# 
# all_data.append(allData_NewClassics)	