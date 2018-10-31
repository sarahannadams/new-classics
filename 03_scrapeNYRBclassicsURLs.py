from bs4 import BeautifulSoup
import requests, json, time, re, csv

book_info_list = []
url_list = []

with open('new_classics.csv','r', encoding="utf-8") as f:
	reader = csv.reader(f)

	#instruct python to ignore headers when reading the data within the csv file
	headers = next(reader)

	for row in reader:
		#how do we assign urls to the variable 
		url = row

		# print("scraping!" + url)
		nyrb_classics_book = requests.get(url)

		#setting the variable for the HTML of the page
		page_html = nyrb_classics_book.text

		#parsing our HTML with BeautifulSoup to give a BeautifulSoup object
		soup = BeautifulSoup(page_html, "html.parser")

		#identifying the 1st parent div that holds the elements we want to scrape
		all_info = soup.find_all("div", attrs={"class":"span8"})

		count=0

		#looping through to pull out the elements we want
		for item in all_info:

			#subtitle is under the span element class=subtitle
			span_subtitle = item.find("span", attrs={"class": "subtitle"})
			subtitle = span_subtitle.text

			# print(subtitle)

			#author and translation information is under the h2 element class=combined-authors
			h2_combined_authors = item.find("h2", attrs={"class": "combined-authors"})
			authors_translation_x = h2_combined_authors.text
			#this line strips the string of any new line carriage returns
			authors_translation_y = authors_translation_x.strip('\n')
			#this line strips the string of any extra spaces
			authors_translation = authors_translation_y.strip()

			# print(authors_translation())

			#identifying the 2nd parent div that holds the elements we want to scrape
			all_info_2 = soup.find_all("div", attrs={"class":"description additional"})

			#looping through to pull out the elements we want
			for item in all_info_2:

				#isbn is under the span element class=variant-sku
				span_variant_sku = item.find("span", attrs={"class": "variant-sku"})
				isbn = span_variant_sku.text

				# print(isbn.strip())

				#publication date is found wihtin additional info, which is under the span p element 
				p_addl_info = item.find("p")
				
				#created a regex to target just the publication date
				x = re.compile('[A-Z][a-z]+ [0-9]+[,] [0-9]+')
				pub_date_x = x.findall(p_addl_info.text)

				#the regex returns the date as a list with only one item. this next line of code targets the list item, rather than the list
				pub_date = pub_date_x[0]

				# print(str(pub_date))

				#adding a count variable so that it counts each loop
				count = count + 1

				#setting up dictionary 
				new_classics_book_info = {}

				#defining keys and values in dictionary
				new_classics_book_info["id"] = count
				new_classics_book_info["subtitle"] = subtitle
				new_classics_book_info["author_translation_note"] = authors_translation
				new_classics_book_info["isbn"] = isbn
				new_classics_book_info["pub_date"] = pub_date		

				#appending our dictionary to our list of books
				book_info_list.append(new_classics_book_info)

			# print(book_info_list)

			#dumping our list of dictionaries into a JSON file
			json.dump(book_info_list, open("new_classics_book_info.json", "w"), indent=2)

		#prints the number of titles to command line (not included in JSON file)	
		print(len(book_info_list))