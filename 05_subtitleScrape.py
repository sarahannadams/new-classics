from bs4 import BeautifulSoup
import requests, json, time, re, csv, time

def subtitle_clean(str_input):

	str_input = str(str_input)
	str_input = str_input.strip('<span class="subtitle">')
	str_input = str_input.strip('</span>')

	return str_input

#create empty list for books
subtitle_info_list = []

#create empty list for book urls
url_list = []

with open('new_classics.csv','r', encoding="utf-8") as f:
	reader = csv.reader(f)

	#instruct python to ignore headers when reading the data within the csv file
	headers = next(reader)

	for row in reader:
		# how do we assign the rows to be the url variable used in the get request?
		url_list.append(row[3])

count = 0

for url in url_list:

	print("scraping!" + url + " " + str(count))
	nyrb_classics_book = requests.get(url)

	#setting the variable for the HTML of the page
	page_html = nyrb_classics_book.text

	#parsing our HTML with BeautifulSoup to give a BeautifulSoup object
	soup = BeautifulSoup(page_html, "html.parser")

	#identifying the parent span that holds the subtitle element we want to scrape
	all_info = soup.find_all("div", attrs={"class":"span8"})

	#looping through to pull out the elements we want
	for item in all_info:

		subtitle = item.find("span", attrs={"class":"subtitle"})
		print(subtitle)

		#adding a count variable so that it counts each loop
		count = count + 1

 	#setting up dictionary 
	subtitle_info = {}

	#defining keys and values in dictionary
	subtitle_info["id"] = count
	subtitle_info["subtitle"] = subtitle_clean(subtitle)
	
	# print(subtitle_info)	

	#appending our dictionary to our list of books
	subtitle_info_list.append(subtitle_info)

	time.sleep(3)

# 	print(subtitle_info_list)

# #dumping our list of dictionaries into a JSON file
json.dump(subtitle_info_list, open("subtitles.json", "w"), indent=2)

#prints the number of titles to command line (not included in JSON file)	
print(len(subtitle_info_list))